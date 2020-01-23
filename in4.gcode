;FLAVOR:Marlin
;TIME:40
;Filament used: 0.00849704m
;l height: 0.25
;MINX:100.2
;MINY:100.2
;MINZ:0.2
;MAXX:119.8
;MAXY:119.8
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
G92 E0
G92 E0
G1 F1500 E-7
;LAYER_COUNT:1
;LAYER:0
M117 l 1 kockatest of 1
M107
;MESH:kockatest.stl
G0 F6000 X100.6 Y119.4 Z0.2
;TYPE:WALL-INNER
G1 F1500 E0
G1 F600 X100.6 Y100.6 E0.47835
G1 X119.4 Y100.6 E0.95669
G1 X119.4 Y119.4 E1.43504
G1 X100.6 Y119.4 E1.91339
G0 F6000 X100.2 Y119.8
;TYPE:WALL-OUTER
G1 F600 X100.2 Y100.2 E2.38276
G1 X119.8 Y100.2 E2.85212
G1 X119.8 Y119.8 E3.32149
G1 X100.2 Y119.8 E3.79086
G0 F6000 X100.67 Y119.33
G0 X102.348 Y119.3
G0 X102.348 Y119.319
;TYPE:FILL
G1 F600 X100.679 Y117.65 E3.85445
G1 X100.397 Y117.368
G0 F6000 X100.7 Y117.368
G0 X100.7 Y114.822
G0 X100.679 Y114.822
G1 F600 X105.177 Y119.319 E4.0258
G1 X105.459 Y119.601
G0 F6000 X105.459 Y119.3
G0 X108.005 Y119.3
G0 X108.005 Y119.319
G1 F600 X100.679 Y111.993 E4.30492
G1 X100.397 Y111.711
G0 F6000 X100.7 Y111.711
G0 X100.7 Y109.165
G0 X100.679 Y109.165
G1 F600 X110.834 Y119.319 E4.69181
G1 X111.116 Y119.601
G0 F6000 X111.116 Y119.3
G0 X113.662 Y119.3
G0 X113.662 Y119.319
G1 F600 X100.679 Y106.336 E5.18646
G1 X100.397 Y106.054
G0 F6000 X100.7 Y106.054
G0 X100.7 Y103.508
G0 X100.679 Y103.508
G1 F600 X116.49 Y119.319 E5.78885
G1 X116.772 Y119.601
G0 F6000 X116.772 Y119.3
G0 X119.3 Y119.319
G0 X119.319 Y119.319
G1 F600 X100.679 Y100.679 E6.49904
G1 X100.397 Y100.397
G0 F6000 X100.67 Y100.67
G0 X103.508 Y100.7
G0 X103.508 Y100.679
G1 F600 X119.319 Y116.49 E7.10144
G1 X119.601 Y116.772
G0 F6000 X119.3 Y116.772
G0 X119.3 Y113.662
G0 X119.319 Y113.662
G1 F600 X106.336 Y100.679 E7.59609
G1 X106.054 Y100.397
G0 F6000 X106.054 Y100.7
G0 X109.165 Y100.7
G0 X109.165 Y100.679
G1 F600 X119.319 Y110.834 E7.98297
G1 X119.601 Y111.116
G0 F6000 X119.3 Y111.116
G0 X119.3 Y108.005
G0 X119.319 Y108.005
G1 F600 X111.993 Y100.679 E8.26209
G1 X111.711 Y100.397
G0 F6000 X111.711 Y100.7
G0 X114.822 Y100.7
G0 X114.822 Y100.679
G1 F600 X119.319 Y105.177 E8.43345
G1 X119.601 Y105.459
G0 F6000 X119.3 Y105.459
G0 X119.3 Y102.348
G0 X119.319 Y102.348
G1 F600 X117.65 Y100.679 E8.49704
G1 X117.368 Y100.397
G0 F6000 X117.368 Y101
;TIME_ELAPSED:40.197757
G1 F1500 E1.49704
M140 S0
M141 S0
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
;SETTING_3 {"global_quality": "[general]\\nversion = 4\\nname = Standard Quality
;SETTING_3  #2\\ndefinition = creality_ender3\\n\\n[metadata]\\nquality_type = s
;SETTING_3 tandard\\ntype = quality_changes\\n\\n[values]\\nadaptive_layer_heigh
;SETTING_3 t_variation = 0.05\\nadhesion_type = none\\nlayer_height = 0.25\\nret
;SETTING_3 raction_combing = all\\nspeed_slowdown_layers = 1\\nsupport_type = ev
;SETTING_3 erywhere\\n\\n", "extruder_quality": ["[general]\\nversion = 4\\nname
;SETTING_3  = Standard Quality #2\\ndefinition = creality_ender3\\n\\n[metadata]
;SETTING_3 \\nposition = 0\\nquality_type = standard\\ntype = quality_changes\\n
;SETTING_3 \\n[values]\\nbottom_layers = 0\\ncoasting_volume = 0.1\\ninfill_mate
;SETTING_3 rial_flow = 90\\ninfill_pattern = lines\\ninfill_wipe_dist = 0.4\\nir
;SETTING_3 oning_flow = 8.0\\nlimit_support_retractions = False\\nmaterial_flow 
;SETTING_3 = 85\\nmaterial_flow_layer_0 = 90\\nmaterial_print_temperature = 195\
;SETTING_3 \nmold_angle = 60\\nraft_margin = 10\\nretract_at_layer_change = True
;SETTING_3 \\nretraction_amount = 7\\nretraction_combing_max_distance = 5\\nretr
;SETTING_3 action_extrusion_window = 7\\nskin_material_flow = 90\\nskin_overlap 
;SETTING_3 = 0\\nskirt_brim_material_flow = 80\\nskirt_gap = 4\\nskirt_line_coun
;SETTING_3 t = 4\\nsmall_hole_max_size = 10\\nspeed_layer_0 = 10.0\\nspeed_print
;SETTING_3  = 50\\nspeed_travel = 180.0\\nsupport_angle = 60\\nsupport_bottom_en
;SETTING_3 able = False\\nsupport_conical_angle = 40\\nsupport_infill_angles = [
;SETTING_3 0 ]\\nsupport_infill_rate = 10\\nsupport_interface_angles = [90 ]\\ns
;SETTING_3 upport_interface_density = 100\\nsupport_interface_pattern = lines\\n
;SETTING_3 support_xy_distance = 1\\ntop_layers = 0\\ntravel_avoid_supports = Fa
;SETTING_3 lse\\nwall_0_material_flow = 80\\nwall_line_count = 2\\nz_seam_corner
;SETTING_3  = z_seam_corner_inner\\n\\n"]}
