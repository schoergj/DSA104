from opentrons import protocol_api

metadata = {
    'protocolName': 'Dual Dye Serial Dilution - 64 Combinations',
    'author': 'OpentronsAI',
    'description': 'Serial dilution for two dyes (yellow and blue) with 8 concentrations each, creating 64 combinations',
    'source': 'OpentronsAI'
}

requirements = {
    'robotType': 'OT-2',
    'apiLevel': '2.25'
}

def run(protocol: protocol_api.ProtocolContext):
    # Load modules
    hs_mod = protocol.load_module('heaterShakerModuleV1', '1')
    
    # Load labware
    # Reservoir for dyes and diluent
    reservoir = protocol.load_labware('opentrons_tough_4_reservoir_72ml', '2')
    
    # Destination plate on heater-shaker
    hs_adapter = hs_mod.load_adapter('opentrons_96_flat_bottom_adapter')
    plate = hs_adapter.load_labware('nest_96_wellplate_200ul_flat')
    
    # Tip racks
    tiprack_1000 = protocol.load_labware('opentrons_flex_96_filtertiprack_1000ul', '4')
    tiprack_20_1 = protocol.load_labware('opentrons_96_tiprack_20ul', '5')
    tiprack_20_2 = protocol.load_labware('opentrons_96_tiprack_20ul', '6')
    
    # Load pipettes
    p1000 = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tiprack_1000])
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20_1, tiprack_20_2])
    
    # Define liquids
    diluent = protocol.define_liquid(
        name='Diluent',
        description='Diluent for serial dilution',
        display_color='#FFFFFF'
    )
    yellow_dye = protocol.define_liquid(
        name='Yellow Dye',
        description='Yellow dye stock solution',
        display_color='#FFFF00'
    )
    blue_dye = protocol.define_liquid(
        name='Blue Dye',
        description='Blue dye stock solution',
        display_color='#0000FF'
    )
    
    # Load liquids into reservoir
    reservoir['A1'].load_liquid(liquid=diluent, volume=70000)  # Diluent
    reservoir['A2'].load_liquid(liquid=yellow_dye, volume=15000)  # Yellow dye
    reservoir['A3'].load_liquid(liquid=blue_dye, volume=15000)  # Blue dye
    
    # Protocol parameters
    diluent_volume = 100  # µL per well
    dye_volume = 100  # µL for initial concentration
    transfer_volume = 100  # µL for serial dilution
    mix_volume = 150  # µL for mixing
    mix_reps = 5
    
    # Close heater-shaker latch
    hs_mod.close_labware_latch()
    
    # Step 1: Add diluent to all wells except first column
    protocol.comment('Adding diluent to wells B1-H8 (for yellow dilution series)')
    p1000.pick_up_tip()
    for row in range(8):  # Rows A-H
        for col in range(1, 8):  # Columns 2-8
            p1000.transfer(
                diluent_volume,
                reservoir['A1'],
                plate.rows()[row][col],
                new_tip='never'
            )
    p1000.drop_tip()
    
    # Step 2: Add yellow dye to first column (A1-H1)
    protocol.comment('Adding yellow dye stock to column 1')
    p1000.pick_up_tip()
    for row in range(8):
        p1000.transfer(
            dye_volume,
            reservoir['A2'],
            plate.rows()[row][0],
            mix_after=(mix_reps, mix_volume),
            new_tip='never'
        )
    p1000.drop_tip()
    
    # Step 3: Perform serial dilution for yellow dye (columns 1-8)
    protocol.comment('Performing serial dilution for yellow dye across columns')
    for row in range(8):
        row_wells = plate.rows()[row]
        # Transfer from column 1 to 2, 2 to 3, etc.
        p20.transfer(
            transfer_volume,
            row_wells[:7],  # Columns 1-7
            row_wells[1:8],  # Columns 2-8
            mix_after=(mix_reps, mix_volume),
            new_tip='always'
        )
    
    # Step 4: Add diluent to columns 9-12 for blue dye dilution
    protocol.comment('Adding diluent to columns 9-12')
    p1000.pick_up_tip()
    for row in range(8):
        for col in range(8, 12):  # Columns 9-12
            p1000.transfer(
                diluent_volume,
                reservoir['A1'],
                plate.rows()[row][col],
                new_tip='never'
            )
    p1000.drop_tip()
    
    # Step 5: Now create blue dye gradient by adding blue dye to rows
    # Row A = highest blue concentration, Row H = lowest
    protocol.comment('Adding blue dye to create concentration gradient across rows')
    
    # Add blue dye stock to all wells in each row, with decreasing amounts
    blue_volumes = [100, 85.7, 71.4, 57.1, 42.9, 28.6, 14.3, 0]  # Decreasing volumes for rows A-H
    
    for row_idx, blue_vol in enumerate(blue_volumes):
        if blue_vol > 0:  # Skip row H (no blue dye)
            p1000.pick_up_tip()
            for col in range(8):  # Add to all 8 yellow concentrations
                p1000.transfer(
                    blue_vol,
                    reservoir['A3'],
                    plate.rows()[row_idx][col],
                    mix_after=(mix_reps, mix_volume),
                    new_tip='never'
                )
            p1000.drop_tip()
    
    # Step 6: Mix on heater-shaker
    protocol.comment('Mixing samples on heater-shaker')
    hs_mod.set_and_wait_for_shake_speed(rpm=1500)
    protocol.delay(minutes=2)
    hs_mod.deactivate_shaker()
    
    protocol.comment('Protocol complete! 64 dye combinations created.')
    protocol.comment('Columns 1-8: Yellow dye concentration gradient (high to low)')
    protocol.comment('Rows A-H: Blue dye concentration gradient (high to low)')