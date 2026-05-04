from opentrons import protocol_api

metadata = {
    'protocolName': '2D Factorial Dilution Series',
    'author': 'OpentronsAI',
    'description': 'Two-dimensional dilution with vertical and horizontal gradients',
    'source': 'OpentronsAI'
}

requirements = {
    'robotType': 'OT-2',
    'apiLevel': '2.25'
}

def run(protocol: protocol_api.ProtocolContext):
    # ========== LABWARE ==========
    # Tip racks
    tiprack_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 10)
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    
    # Reservoir for reagents
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', 2)
    
    # Destination plate
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', 3)
    
    # ========== PIPETTES ==========
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tiprack_1000])
    p300 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack_300])
    
    # ========== PARAMETERS ==========
    # Reagent locations in reservoir
    reagent_a = reservoir['A1']  # First dye/reagent (vertical dilution)
    reagent_b = reservoir['A2']  # Second dye/reagent (vertical dilution, opposite direction)
    diluent = reservoir['A3']    # Diluent (water)
    
    # Volumes
    total_volume = 200  # Final volume in each well (µL)
    transfer_volume = 100  # Volume for serial dilution (µL)
    
    # Dilution ratios
    vertical_dilution_factor = 2  # 1:2 dilution vertically
    horizontal_dilution_factor = 2  # 1:2 dilution horizontally
    
    # ========== PROTOCOL STEPS ==========
    
    # Step 1: Add diluent to all wells except row A and column 1
    protocol.comment("Step 1: Adding diluent to dilution wells")
    p1000.pick_up_tip()
    for row_idx in range(1, 8):  # Rows B-H
        for col_idx in range(1, 12):  # Columns 2-12
            well = plate.rows()[row_idx][col_idx]
            p1000.transfer(transfer_volume, diluent, well, new_tip='never')
    p1000.drop_tip()
    
    # Step 2: Add reagent A to column 1 (rows A-G) - vertical gradient top to bottom
    protocol.comment("Step 2: Adding Reagent A to column 1 (vertical gradient)")
    p1000.pick_up_tip()
    for row_idx in range(7):  # Rows A-G
        well = plate.rows()[row_idx][0]
        p1000.transfer(total_volume, reagent_a, well, new_tip='never')
    p1000.drop_tip()
    
    # Step 3: Add reagent B to column 1 (row H) - opposite direction
    protocol.comment("Step 3: Adding Reagent B to column 1 (row H)")
    p1000.transfer(total_volume, reagent_b, plate['H1'], new_tip='always')
    
    # Step 4: Add reagent B to row A (columns 2-11) - horizontal gradient
    protocol.comment("Step 4: Adding Reagent B to row A (horizontal gradient)")
    p1000.pick_up_tip()
    for col_idx in range(1, 11):  # Columns 2-11
        well = plate.rows()[0][col_idx]
        p1000.transfer(transfer_volume, reagent_b, well, new_tip='never')
    p1000.drop_tip()
    
    # Step 5: Add water blank to row H (columns 2-12)
    protocol.comment("Step 5: Adding water blank to row H")
    p1000.pick_up_tip()
    for col_idx in range(1, 12):  # Columns 2-12
        well = plate.rows()[7][col_idx]
        p1000.transfer(transfer_volume, diluent, well, new_tip='never')
    p1000.drop_tip()
    
    # Step 6: Vertical serial dilution (column 1, rows A-G)
    protocol.comment("Step 6: Performing vertical serial dilution in column 1")
    p1000.pick_up_tip()
    for row_idx in range(6):  # Rows A-F to B-G
        source = plate.rows()[row_idx][0]
        dest = plate.rows()[row_idx + 1][0]
        p1000.transfer(transfer_volume, source, dest, 
                      mix_after=(3, 50), new_tip='never')
    p1000.drop_tip()
    
    # Step 7: Horizontal serial dilution using multi-channel (rows A-G)
    protocol.comment("Step 7: Performing horizontal serial dilution")
    # For rows A-G, perform horizontal dilution
    for col_idx in range(10):  # Columns 1-10 to 2-11
        p300.pick_up_tip()
        source_col = plate.columns()[col_idx]
        dest_col = plate.columns()[col_idx + 1]
        # Transfer from current column to next, mix in destination
        p300.transfer(transfer_volume, source_col[0], dest_col[0],
                     mix_after=(3, 50), new_tip='never')
        p300.drop_tip()
    
    # Step 8: Final mixing to ensure homogeneity
    protocol.comment("Step 8: Final mixing of all wells")
    for row_idx in range(7):  # Rows A-G
        p300.pick_up_tip()
        for col_idx in range(11):  # Columns 1-11
            well = plate.rows()[row_idx][col_idx]
            p300.mix(3, 100, well)
        p300.drop_tip()
    
    protocol.comment("Protocol complete! 2D dilution series created.")
    protocol.comment("Vertical: Reagent A gradient (A1-G1) with opposite Reagent B (H1)")
    protocol.comment("Horizontal: Reagent B gradient (A2-A11) with factorial dilution")
    protocol.comment("Row H: Water blanks (H2-H12)")