import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "OT2-DSA104-Demo",
    "author": "JS",
    "description": "Built on the DSA102 protocol for exploring pipetting options (2026 version) to test simulations and explore the python scripts behind the protocols.",
    "created": "2025-02-05T10:39:20.313Z",
    "internalAppBuildDate": "Tue, 24 Mar 2026 15:51:09 GMT",
    "lastModified": "2026-04-22T06:36:50.319Z",
    "protocolDesigner": "8.9.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_tiprack_1000ul",
        location="9",
        label="Opentrons OT-2 96 Tip Rack 1000 µL (1)",
        namespace="opentrons",
        version=1,
    )
    tube_rack_1 = protocol.load_labware(
        "opentrons_15_tuberack_falcon_15ml_conical",
        location="7",
        namespace="opentrons",
        version=3,
    )
    tube_rack_2 = protocol.load_labware(
        "opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap",
        location="3",
        namespace="opentrons",
        version=3,
    )
    well_plate_1 = protocol.load_labware(
        "corning_96_wellplate_360ul_flat",
        location="1",
        namespace="opentrons",
        version=5,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_96_tiprack_300ul",
        location="5",
        namespace="opentrons",
        version=1,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p1000_single_gen2", "left")
    pipette_right = protocol.load_instrument("p300_multi_gen2", "right")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "Water",
        display_color="#b925ff",
    )
    liquid_2 = protocol.define_liquid(
        "Glycerol/Water 4/1",
        display_color="#ffd600",
    )
    liquid_3 = protocol.define_liquid(
        "EtOAc",
        display_color="#9dffd8",
    )

    # Load Liquids:
    tube_rack_1.load_liquid(
        wells=["A1"],
        liquid=liquid_1,
        volume=7000,
    )
    tube_rack_1.load_liquid(
        wells=["B1"],
        liquid=liquid_2,
        volume=7000,
    )
    tube_rack_1.load_liquid(
        wells=["C1"],
        liquid=liquid_3,
        volume=7000,
    )

    # PROTOCOL STEPS

    # Step 1: pause
    protocol.pause("Check your deck, tips, labware and liquids. Then close the lid.")

    # Step 2: Transfer -  Touch Tip
    pipette_left.transfer_with_liquid_class(
        volume=500,
        source=[tube_rack_1["C1"]],
        dest=[tube_rack_2["A2"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p1000_single_gen2": {"opentrons/opentrons_96_tiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -1,
                            "mm_from_edge": 0,
                            "speed": 80,
                        },
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -1,
                            "mm_from_edge": 0,
                            "speed": 80,
                        },
                        "blowout": {
                            "enabled": True,
                            "location": "destination",
                            "flow_rate": 274.7,
                        },
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 3: Transfer -  Delay
    pipette_left.transfer_with_liquid_class(
        volume=500,
        source=[tube_rack_1["C1"]],
        dest=[tube_rack_2["A3"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p1000_single_gen2": {"opentrons/opentrons_96_tiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 2},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 2},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -1,
                            "mm_from_edge": 0,
                            "speed": 80,
                        },
                        "blowout": {
                            "enabled": True,
                            "location": "destination",
                            "flow_rate": 274.7,
                        },
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 4: Transfer -  Airgap 100uL
    # Delay for better visualization
    pipette_left.transfer_with_liquid_class(
        volume=500,
        source=[tube_rack_1["C1"]],
        dest=[tube_rack_2["A4"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_4",
            properties={"p1000_single_gen2": {"opentrons/opentrons_96_tiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 100)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -1,
                            "mm_from_edge": 0,
                            "speed": 80,
                        },
                        "blowout": {
                            "enabled": True,
                            "location": "destination",
                            "flow_rate": 274.7,
                        },
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 5: Transfer -  Pre-Wet Tip
    # Delay for better visualization
    pipette_left.transfer_with_liquid_class(
        volume=500,
        source=[tube_rack_1["C1"]],
        dest=[tube_rack_2["A5"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_5",
            properties={"p1000_single_gen2": {"opentrons/opentrons_96_tiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 1},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 25},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "delay": {"enabled": True, "duration": 1},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": True, "duration": 1},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {
                            "enabled": True,
                            "z_offset": -1,
                            "mm_from_edge": 0,
                            "speed": 80,
                        },
                        "blowout": {
                            "enabled": True,
                            "location": "destination",
                            "flow_rate": 274.7,
                        },
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 6: pause
    protocol.pause("Open the lid and close the vials with EtOAc, then close the lid and continue.")

    # Step 7: transfer
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[tube_rack_2["A2"], tube_rack_2["A3"], tube_rack_2["A4"], tube_rack_2["A5"]],
        dest=[well_plate_1["A1"], well_plate_1["A2"], well_plate_1["A3"], well_plate_1["A4"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
            properties={"p1000_single_gen2": {"opentrons/opentrons_96_tiprack_1000ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 274.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 8: transfer
    pipette_right.configure_nozzle_layout(
        protocol_api.SINGLE,
        start="H1",
    )
    pipette_right.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"], well_plate_1["A1"]],
        dest=[well_plate_1["C1"], well_plate_1["C2"], well_plate_1["C3"], well_plate_1["C4"], well_plate_1["C5"], well_plate_1["C6"], well_plate_1["C7"], well_plate_1["C8"], well_plate_1["C9"], well_plate_1["C10"], well_plate_1["C11"], well_plate_1["C12"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_8",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_tiprack_300ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.9.0","data":{"pipetteTiprackAssignments":{"4c960657-0009-47e7-9b73-a2bbfc681874":["opentrons/opentrons_96_tiprack_1000ul/1"],"2b10a0d6-b163-4bb6-886f-1ff01a13b904":["opentrons/opentrons_96_tiprack_300ul/1"]},"dismissedWarnings":{"form":[],"timeline":[]},"ingredients":{"0":{"displayName":"Water","description":null,"liquidGroupId":"0","displayColor":"#b925ff","liquidClass":null},"1":{"displayName":"Glycerol/Water 4/1","description":null,"liquidGroupId":"1","displayColor":"#ffd600","liquidClass":null},"2":{"displayName":"EtOAc","description":null,"liquidGroupId":"2","displayColor":"#9dffd8","liquidClass":null}},"ingredLocations":{"a35debc4-9e6d-45fc-94da-e29e3f3abb97:opentrons/opentrons_15_tuberack_falcon_15ml_conical/3":{"A1":{"0":{"volume":7000}},"B1":{"1":{"volume":7000}},"C1":{"2":{"volume":7000}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"0eaf3765-4be2-41f3-aacf-4288a7a297af:opentrons/opentrons_96_tiprack_1000ul/1":"9","a35debc4-9e6d-45fc-94da-e29e3f3abb97:opentrons/opentrons_15_tuberack_falcon_15ml_conical/3":"7","e1b24a0e-f075-49a6-a4c4-be2231a2c5a8:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3":"3","6023fef3-94ba-4666-9585-a0abfadb6cab:opentrons/corning_96_wellplate_360ul_flat/5":"1","6c651489-5d31-4a5e-a40d-fe27535504bd:opentrons/opentrons_96_tiprack_300ul/1":"5"},"moduleLocationUpdate":{},"pipetteLocationUpdate":{"4c960657-0009-47e7-9b73-a2bbfc681874":"left","2b10a0d6-b163-4bb6-886f-1ff01a13b904":"right"},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"wasteChuteLocationUpdate":{},"trashBinLocationUpdate":{"f8f58702-edd4-44f3-ac5b-a567969792dc:trashBin":"cutout12"},"moduleStateUpdate":{}},"84e03ef4-970c-4b0b-8fda-67adfa960c89":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Check your deck, tips, labware and liquids. Then close the lid.","pauseTemperature":null,"pauseTime":null,"id":"84e03ef4-970c-4b0b-8fda-67adfa960c89","stepType":"pause","stepName":"pause","stepDetails":""},"3e508e58-d9dd-421a-98e7-02160de77880":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":274.7,"aspirate_labware":"a35debc4-9e6d-45fc-94da-e29e3f3abb97:opentrons/opentrons_15_tuberack_falcon_15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":25,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":true,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":"80","aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":274.7,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":274.7,"dispense_labware":"e1b24a0e-f075-49a6-a4c4-be2231a2c5a8:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":25,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":true,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"80","dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"f8f58702-edd4-44f3-ac5b-a567969792dc:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"SINGLE","path":"single","pipette":"4c960657-0009-47e7-9b73-a2bbfc681874","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"500","stepType":"moveLiquid","stepName":"Transfer -  Touch Tip","stepDetails":"","id":"3e508e58-d9dd-421a-98e7-02160de77880","dispense_touchTip_mmfromTop":null},"9adf5e20-4950-4df1-b914-598abbe8417e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"2","aspirate_flowRate":274.7,"aspirate_labware":"a35debc4-9e6d-45fc-94da-e29e3f3abb97:opentrons/opentrons_15_tuberack_falcon_15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":25,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"2","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":274.7,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":274.7,"dispense_labware":"e1b24a0e-f075-49a6-a4c4-be2231a2c5a8:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":25,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":true,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"80","dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"f8f58702-edd4-44f3-ac5b-a567969792dc:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"SINGLE","path":"single","pipette":"4c960657-0009-47e7-9b73-a2bbfc681874","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"500","stepType":"moveLiquid","stepName":"Transfer -  Delay","stepDetails":"","id":"9adf5e20-4950-4df1-b914-598abbe8417e","dispense_touchTip_mmfromTop":null},"2da02a6a-0c63-4266-9015-bbb4314dbbe4":{"aspirate_airGap_checkbox":true,"aspirate_airGap_volume":"100","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":274.7,"aspirate_labware":"a35debc4-9e6d-45fc-94da-e29e3f3abb97:opentrons/opentrons_15_tuberack_falcon_15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":25,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":274.7,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":274.7,"dispense_labware":"e1b24a0e-f075-49a6-a4c4-be2231a2c5a8:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":25,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":true,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"80","dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"f8f58702-edd4-44f3-ac5b-a567969792dc:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"SINGLE","path":"single","pipette":"4c960657-0009-47e7-9b73-a2bbfc681874","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"500","stepType":"moveLiquid","stepName":"Transfer -  Airgap 100uL","stepDetails":"Delay for better visualization","id":"2da02a6a-0c63-4266-9015-bbb4314dbbe4","dispense_touchTip_mmfromTop":null},"5b1d33ae-8181-4e78-867d-b46b25649557":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"100","aspirate_delay_checkbox":true,"aspirate_delay_seconds":"1","aspirate_flowRate":274.7,"aspirate_labware":"a35debc4-9e6d-45fc-94da-e29e3f3abb97:opentrons/opentrons_15_tuberack_falcon_15ml_conical/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":25,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["C1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":274.7,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":true,"dispense_delay_seconds":"1","dispense_flowRate":274.7,"dispense_labware":"e1b24a0e-f075-49a6-a4c4-be2231a2c5a8:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":25,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"1","dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":true,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":"80","dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"f8f58702-edd4-44f3-ac5b-a567969792dc:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"SINGLE","path":"single","pipette":"4c960657-0009-47e7-9b73-a2bbfc681874","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_tiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"500","stepType":"moveLiquid","stepName":"Transfer -  Pre-Wet Tip","stepDetails":"Delay for better visualization","id":"5b1d33ae-8181-4e78-867d-b46b25649557","dispense_touchTip_mmfromTop":null},"4c1eab73-4678-4d25-bd50-88d9307bae99":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Open the lid and close the vials with EtOAc, then close the lid and continue.","pauseTemperature":null,"pauseTime":null,"id":"4c1eab73-4678-4d25-bd50-88d9307bae99","stepType":"pause","stepName":"pause","stepDetails":""},"49209a2a-734e-4224-a961-3ec1f5471396":{"id":"49209a2a-734e-4224-a961-3ec1f5471396","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"274.7","aspirate_labware":"e1b24a0e-f075-49a6-a4c4-be2231a2c5a8:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2","A3","A4","A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"274.7","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"274.7","dispense_labware":"6023fef3-94ba-4666-9585-a0abfadb6cab:opentrons/corning_96_wellplate_360ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","A2","A3","A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"f8f58702-edd4-44f3-ac5b-a567969792dc:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":null,"path":"single","pipette":"4c960657-0009-47e7-9b73-a2bbfc681874","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_1000ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200"},"f3276435-e763-41d7-8211-3c352b756964":{"id":"f3276435-e763-41d7-8211-3c352b756964","stepType":"moveLiquid","stepName":"transfer","stepDetails":"","stepNumber":0,"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"94","aspirate_labware":"6023fef3-94ba-4666-9585-a0abfadb6cab:opentrons/corning_96_wellplate_360ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"","aspirate_mix_volume":null,"aspirate_mmFromBottom":null,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":"0","aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":"125","aspirate_retract_x_position":0,"aspirate_retract_y_position":0,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":"0","aspirate_submerge_speed":"125","aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":0,"aspirate_submerge_y_position":0,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":60,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":"94","blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"94","dispense_labware":"6023fef3-94ba-4666-9585-a0abfadb6cab:opentrons/corning_96_wellplate_360ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":"","dispense_mix_volume":null,"dispense_mmFromBottom":null,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":"0","dispense_retract_mmFromBottom":2,"dispense_retract_speed":"125","dispense_retract_x_position":0,"dispense_retract_y_position":0,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":"0","dispense_submerge_speed":"125","dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":0,"dispense_submerge_y_position":0,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":60,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"f8f58702-edd4-44f3-ac5b-a567969792dc:trashBin","liquidClassesSupported":true,"liquidClass":"none","nozzles":"SINGLE","path":"single","pipette":"2b10a0d6-b163-4bb6-886f-1ff01a13b904","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":"0","tipRack":"opentrons/opentrons_96_tiprack_300ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10"}},"orderedStepIds":["84e03ef4-970c-4b0b-8fda-67adfa960c89","3e508e58-d9dd-421a-98e7-02160de77880","9adf5e20-4950-4df1-b914-598abbe8417e","2da02a6a-0c63-4266-9015-bbb4314dbbe4","5b1d33ae-8181-4e78-867d-b46b25649557","4c1eab73-4678-4d25-bd50-88d9307bae99","49209a2a-734e-4224-a961-3ec1f5471396","f3276435-e763-41d7-8211-3c352b756964"],"pipettes":{"4c960657-0009-47e7-9b73-a2bbfc681874":{"pipetteName":"p1000_single_gen2"},"2b10a0d6-b163-4bb6-886f-1ff01a13b904":{"pipetteName":"p300_multi_gen2"}},"modules":{},"labware":{"0eaf3765-4be2-41f3-aacf-4288a7a297af:opentrons/opentrons_96_tiprack_1000ul/1":{"displayName":"Opentrons OT-2 96 Tip Rack 1000 µL (1)","labwareDefURI":"opentrons/opentrons_96_tiprack_1000ul/1"},"a35debc4-9e6d-45fc-94da-e29e3f3abb97:opentrons/opentrons_15_tuberack_falcon_15ml_conical/3":{"displayName":"Opentrons 15 Tube Rack with Falcon 15 mL Conical","labwareDefURI":"opentrons/opentrons_15_tuberack_falcon_15ml_conical/3"},"e1b24a0e-f075-49a6-a4c4-be2231a2c5a8:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3":{"displayName":"Opentrons 24 Tube Rack with Eppendorf 1.5 mL Safe-Lock Snapcap","labwareDefURI":"opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/3"},"6023fef3-94ba-4666-9585-a0abfadb6cab:opentrons/corning_96_wellplate_360ul_flat/5":{"displayName":"Corning 96 Well Plate 360 µL Flat","labwareDefURI":"opentrons/corning_96_wellplate_360ul_flat/5"},"6c651489-5d31-4a5e-a40d-fe27535504bd:opentrons/opentrons_96_tiprack_300ul/1":{"displayName":"Opentrons OT-2 96 Tip Rack 300 µL","labwareDefURI":"opentrons/opentrons_96_tiprack_300ul/1"}}}},"metadata":{"protocolName":"OT2-DSA104-Demo","author":"JS","description":"Built on the DSA102 protocol for exploring pipetting options (2026 version) to test simulations and explore the python scripts behind the protocols.","created":1738751960313,"lastModified":1776839810319,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
