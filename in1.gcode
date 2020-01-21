;FLAVOR:Marlin
;TIME:111
;Filament used: 0.027521m
;l height: 0.25
;MINX:90.2
;MINY:90.2
;MINZ:0.2
;MAXX:129.8
;MAXY:129.8
;MAXZ:0.2
;POSTPROCESSED
;Generated with Cura_SteamEngine 4.4.0
M140 S60
M105
M190 S60
M104 S195
M105
M109 S195
M82 ;absolute extrusion mode
M201 X500.00 Y500.00 Z100.00 E5000.00 ;Setup machine max acceleration
M203 X500.00 Y500.00 Z10.00 E50.00 ;Setup machine max feedrate
M204 P500.00 R1000.00 T500.00 ;Setup Print/Retract/Travel acceleration
M205 X8.00 Y8.00 Z0.40 E5.00 ;Setup Jerk
M220 S100 ;Reset Feedrate
M221 S100 ;Reset Flowrate

G28 ;Home

G92 E0 ;Reset Extruder
G1 Z2.0 F3000 ;Move Z Axis up
G1 X10.1 Y20 Z0.28 F5000.0 ;Move to start position
G1 X10.1 Y200.0 Z0.28 F1500.0 E15 ;Draw the first line
G1 X10.4 Y200.0 Z0.28 F5000.0 ;Move to side a little
G1 X10.4 Y20 Z0.28 F1500.0 E30 ;Draw the second line
G92 E0 ;Reset Extruder
G1 Z2.0 F3000 ;Move Z Axis up

M141 S28
M83 ;relative extrusion mode
G1 F1500 E-7
;LAYER_COUNT:1
;LAYER:0
M117 l 1 kockatest of 1
M107
;MESH:kockatest.stl
G0 F6000 X90.6 Y129.4 Z0.2
;TYPE:WALL-INNER
G1 F1500 E7
G1 F600 X90.6 Y90.6 E0.98723
G1 X129.4 Y90.6 E0.98723
G1 X129.4 Y129.4 E0.98723
G1 X90.6 Y129.4 E0.98723
G0 F6000 X90.2 Y129.8
;TYPE:WALL-OUTER
G1 F600 X90.2 Y90.2 E0.94831
G1 X129.8 Y90.2 E0.94831
G1 X129.8 Y129.8 E0.94831
G1 X90.2 Y129.8 E0.94831
G0 F6000 X90.67 Y129.33
G0 X90.7 Y128
G0 X90.679 Y128
;TYPE:FILL
G1 F600 X129.319 Y128 E1.04099
G0 F6000 X129.3 Y128
G0 X129.3 Y126
G0 X129.319 Y126
G1 F600 X90.679 Y126 E1.04099
G0 F6000 X90.7 Y126
G0 X90.7 Y124
G0 X90.679 Y124
G1 F600 X129.319 Y124 E1.04099
G0 F6000 X129.3 Y124
G0 X129.3 Y122
G0 X129.319 Y122
G1 F600 X90.679 Y122 E1.04099
G0 F6000 X90.7 Y122
G0 X90.7 Y120
G0 X90.679 Y120
G1 F600 X129.319 Y120 E1.04099
G0 F6000 X129.3 Y120
G0 X129.3 Y118
G0 X129.32 Y118
G1 F600 X90.68 Y118 E1.04099
G0 F6000 X90.7 Y118
G0 X90.7 Y116
G0 X90.68 Y116
G1 F600 X129.32 Y116 E1.04099
G0 F6000 X129.3 Y116
G0 X129.3 Y114
G0 X129.32 Y114
G1 F600 X90.68 Y114 E1.04099
G0 F6000 X90.7 Y114
G0 X90.7 Y112
G0 X90.68 Y112
G1 F600 X129.32 Y112 E1.04099
G0 F6000 X129.3 Y112
G0 X129.3 Y110
G0 X129.32 Y110
G1 F600 X90.68 Y110 E1.04099
G0 F6000 X90.7 Y110
G0 X90.7 Y108
G0 X90.68 Y108
G1 F600 X129.32 Y108 E1.04099
G0 F6000 X129.3 Y108
G0 X129.3 Y106
G0 X129.32 Y106
G1 F600 X90.68 Y106 E1.04099
G0 F6000 X90.7 Y106
G0 X90.7 Y104
G0 X90.68 Y104
G1 F600 X129.32 Y104 E1.04099
G0 F6000 X129.3 Y104
G0 X129.3 Y102
G0 X129.32 Y102
G1 F600 X90.68 Y102 E1.04099
G0 F6000 X90.7 Y102
G0 X90.7 Y100
G0 X90.68 Y100
G1 F600 X129.32 Y100 E1.04099
G0 F6000 X129.3 Y100
G0 X129.3 Y98
G0 X129.32 Y98
G1 F600 X90.68 Y98 E1.04099
G0 F6000 X90.7 Y98
G0 X90.7 Y96
G0 X90.68 Y96
G1 F600 X129.32 Y96 E1.04099
G0 F6000 X129.3 Y96
G0 X129.3 Y94
G0 X129.32 Y94
G1 F600 X90.68 Y94 E1.04099
G0 F6000 X90.7 Y94
G0 X90.7 Y92
G0 X90.68 Y92
G1 F600 X129.32 Y92 E1.04099
G0 F6000 X129 Y92
;TIME_ELAPSED:111.794644
G1 F1500 E-7
M140 S0
M141 S0
M82 ;absolute extrusion mode
G91 ;Relative positioning
G1 E-2 F2700 ;Retract a bit
G1 E-2 Z0.2 F2400 ;Retract and raise Z
G1 X5 Y5 F3000 ;Wipe out
G1 Z10 ;Raise Z more
G90 ;Absolute positionning

G1 X0 Y220 ;Present print
M106 S0 ;Turn-off fan
M104 S0 ;Turn-off hotend
M140 S0 ;Turn-off bed

M84 X Y E ;Disable all steppers but Z

M82 ;absolute extrusion mode
M104 S0
;End of Gcode
;SETTING_3 {"extruder_quality": ["[general]\\nversion = 4\\nname = Standard Qual
;SETTING_3 ity #2\\ndefinition = creality_ender3\\n\\n[metadata]\\ntype = qualit
;SETTING_3 y_changes\\nquality_type = standard\\nposition = 0\\n\\n[values]\\nbo
;SETTING_3 ttom_layers = 0\\ncoasting_volume = 0.1\\ninfill_angles = [90]\\ninfi
;SETTING_3 ll_material_flow = 90\\ninfill_pattern = lines\\nironing_flow = 8.0\\
;SETTING_3 nlimit_support_retractions = False\\nmaterial_flow = 85\\nmaterial_fl
;SETTING_3 ow_layer_0 = 90\\nmaterial_print_temperature = 195\\nmold_angle = 60\
;SETTING_3 \nraft_margin = 10\\nretract_at_layer_change = True\\nretraction_amou
;SETTING_3 nt = 7\\nretraction_combing_max_distance = 5\\nretraction_extrusion_w
;SETTING_3 indow = 7\\nskin_material_flow = 90\\nskin_overlap = 0\\nskirt_brim_m
;SETTING_3 aterial_flow = 80\\nskirt_gap = 4\\nskirt_line_count = 4\\nsmall_hole
;SETTING_3 _max_size = 10\\nspeed_layer_0 = 10.0\\nspeed_print = 50\\nspeed_trav
;SETTING_3 el = 180.0\\nsupport_angle = 60\\nsupport_bottom_enable = False\\nsup
;SETTING_3 port_conical_angle = 40\\nsupport_infill_angles = [0 ]\\nsupport_infi
;SETTING_3 ll_rate = 10\\nsupport_interface_angles = [90 ]\\nsupport_interface_d
;SETTING_3 ensity = 100\\nsupport_interface_pattern = lines\\nsupport_xy_distanc
;SETTING_3 e = 1\\ntop_layers = 0\\ntravel_avoid_supports = False\\nwall_0_mater
;SETTING_3 ial_flow = 80\\nwall_line_count = 2\\nz_seam_corner = z_seam_corner_i
;SETTING_3 nner\\n\\n"], "global_quality": "[general]\\nversion = 4\\nname = Sta
;SETTING_3 ndard Quality #2\\ndefinition = creality_ender3\\n\\n[metadata]\\ntyp
;SETTING_3 e = quality_changes\\nquality_type = standard\\n\\n[values]\\nadaptiv
;SETTING_3 e_layer_height_variation = 0.05\\nadhesion_type = none\\nlayer_height
;SETTING_3  = 0.25\\nrelative_extrusion = True\\nretraction_combing = all\\nspee
;SETTING_3 d_slowdown_layers = 1\\nsupport_type = everywhere\\n\\n"}
