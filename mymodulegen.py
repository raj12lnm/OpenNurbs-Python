from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers


import pybindgen.settings
import warnings

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        warnings.warn("exception %r in wrapper %s" % (exception, wrapper))
        return True
pybindgen.settings.error_handler = ErrorHandler()


import sys

def module_init():
    root_module = Module('opennurbs', cpp_namespace='::')
    root_module.add_include('"opennurbs.h"')
    return root_module

def register_types(module):
    root_module = module.get_root()
    
    module.add_class('ON')
    module.add_enum('knot_style', ['unknown_knot_style', 'uniform_knots', 'quasi_uniform_knots', 'piecewise_bezier_knots', 'clamped_end_knots', 'non_uniform_knots', 'knot_style_count'], outer_class=root_module['ON'])
    module.add_enum('sort_algorithm', ['heap_sort', 'quick_sort'], outer_class=root_module['ON'])
    module.add_enum('view_projection', ['unknown_view', 'parallel_view', 'perspective_view'], outer_class=root_module['ON'])
    module.add_enum('eAnnotationType', ['dtNothing', 'dtDimLinear', 'dtDimAligned', 'dtDimAngular', 'dtDimDiameter', 'dtDimRadius', 'dtLeader', 'dtTextBlock', 'dtDimOrdinate'], outer_class=root_module['ON'])
    module.add_enum('eTextDisplayMode', ['dtNormal', 'dtHorizontal', 'dtAboveLine', 'dtInLine'], outer_class=root_module['ON'])
    module.add_enum('active_space', ['no_space', 'model_space', 'page_space'], outer_class=root_module['ON'])
    module.add_enum('unit_system', ['no_unit_system', 'angstroms', 'nanometers', 'microns', 'millimeters', 'centimeters', 'decimeters', 'meters', 'dekameters', 'hectometers', 'kilometers', 'megameters', 'gigameters', 'microinches', 'mils', 'inches', 'feet', 'yards', 'miles', 'printer_point', 'printer_pica', 'nautical_mile', 'astronomical', 'lightyears', 'parsecs', 'custom_unit_system'], outer_class=root_module['ON'])
    module.add_enum('distance_display_mode', ['decimal', 'fractional', 'feet_inches'], outer_class=root_module['ON'])
    module.add_enum('point_style', ['unknown_point_style', 'not_rational', 'homogeneous_rational', 'euclidean_rational', 'intrinsic_point_style', 'point_style_count'], outer_class=root_module['ON'])
    module.add_enum('continuity', ['unknown_continuity', 'C0_continuous', 'C1_continuous', 'C2_continuous', 'G1_continuous', 'G2_continuous', 'C0_locus_continuous', 'C1_locus_continuous', 'C2_locus_continuous', 'G1_locus_continuous', 'G2_locus_continuous', 'Cinfinity_continuous', 'Gsmooth_continuous'], outer_class=root_module['ON'])
    module.add_enum('curve_style', ['unknown_curve_style', 'line', 'circle', 'ellipse', 'parabola', 'hyperbola', 'planar_polyline', 'polyline', 'planar_freeform_curve', 'freeform_curve', 'curve_style_count'], outer_class=root_module['ON'])
    module.add_enum('surface_style', ['unknown_surface_style', 'plane', 'circular_cylinder', 'elliptical_cylinder', 'circular_cone', 'elliptical_cone', 'sphere', 'torus', 'surface_of_revolution', 'ruled_surface', 'freeform_surface', 'surface_style_count'], outer_class=root_module['ON'])
    module.add_enum('endian', ['little_endian', 'big_endian'], outer_class=root_module['ON'])
    module.add_enum('archive_mode', ['unknown_archive_mode', 'read', 'write', 'readwrite', 'read3dm', 'write3dm'], outer_class=root_module['ON'])
    module.add_enum('coordinate_system', ['world_cs', 'camera_cs', 'clip_cs', 'screen_cs'], outer_class=root_module['ON'])
    module.add_enum('exception_type', ['unknown_exception', 'out_of_memory', 'corrupt_object', 'unable_to_write_archive', 'unable_to_read_archive', 'unable_to_seek_archive', 'unexpected_end_of_archive', 'unexpected_value_in_archive'], outer_class=root_module['ON'])
    module.add_enum('layer_mode', ['normal_layer', 'hidden_layer', 'locked_layer', 'layer_mode_count'], outer_class=root_module['ON'])
    module.add_enum('object_mode', ['normal_object', 'hidden_object', 'locked_object', 'idef_object', 'object_mode_count'], outer_class=root_module['ON'])
    module.add_enum('object_color_source', ['color_from_layer', 'color_from_object', 'color_from_material', 'color_from_parent'], outer_class=root_module['ON'])
    module.add_enum('plot_color_source', ['plot_color_from_layer', 'plot_color_from_object', 'plot_color_from_display', 'plot_color_from_parent'], outer_class=root_module['ON'])
    module.add_enum('plot_weight_source', ['plot_weight_from_layer', 'plot_weight_from_object', 'plot_weight_from_parent'], outer_class=root_module['ON'])
    module.add_enum('object_linetype_source', ['linetype_from_layer', 'linetype_from_object', 'linetype_from_parent'], outer_class=root_module['ON'])
    module.add_enum('object_material_source', ['material_from_layer', 'material_from_object', 'material_from_parent'], outer_class=root_module['ON'])
    module.add_enum('light_style', ['unknown_light_style', 'camera_directional_light', 'camera_point_light', 'camera_spot_light', 'world_directional_light', 'world_point_light', 'world_spot_light', 'ambient_light', 'world_linear_light', 'world_rectangular_light', 'light_style_count'], outer_class=root_module['ON'])
    module.add_enum('curvature_style', ['unknown_curvature_style', 'gaussian_curvature', 'mean_curvature', 'min_curvature', 'max_curvature', 'curvature_style_count'], outer_class=root_module['ON'])
    module.add_enum('display_mode', ['default_display', 'wireframe_display', 'shaded_display', 'renderpreview_display'], outer_class=root_module['ON'])
    module.add_enum('view_type', ['model_view_type', 'page_view_type', 'nested_view_type'], outer_class=root_module['ON'])
    module.add_enum('texture_mode', ['no_texture', 'modulate_texture', 'decal_texture'], outer_class=root_module['ON'])
    module.add_enum('object_type', ['unknown_object_type', 'point_object', 'pointset_object', 'curve_object', 'surface_object', 'brep_object', 'mesh_object', 'layer_object', 'material_object', 'light_object', 'annotation_object', 'userdata_object', 'instance_definition', 'instance_reference', 'text_dot', 'grip_object', 'detail_object', 'hatch_object', 'morph_control_object', 'loop_object', 'polysrf_filter', 'edge_filter', 'polyedge_filter', 'meshvertex_object', 'meshedge_object', 'meshface_object', 'cage_object', 'phantom_object', 'clipplane_object', 'beam_object', 'extrusion_object', 'any_object'], outer_class=root_module['ON'])
    module.add_enum('bitmap_type', ['unknown_bitmap_type', 'windows_bitmap', 'opengl_bitmap', 'png_bitmap'], outer_class=root_module['ON'])
    module.add_enum('object_decoration', ['no_object_decoration', 'start_arrowhead', 'end_arrowhead', 'both_arrowhead'], outer_class=root_module['ON'])
    module.add_enum('mesh_type', ['default_mesh', 'render_mesh', 'analysis_mesh', 'preview_mesh', 'any_mesh'], outer_class=root_module['ON'])
    module.add_enum('osnap_mode', ['os_none', 'os_near', 'os_focus', 'os_center', 'os_vertex', 'os_knot', 'os_quadrant', 'os_midpoint', 'os_intersection', 'os_end', 'os_perpendicular', 'os_tangent', 'os_point', 'os_all_snaps'], outer_class=root_module['ON'])
    module.add_enum('eCurveType', ['ctCurve', 'ctArc', 'ctCircle', 'ctLine', 'ctNurbs', 'ctOnsurface', 'ctProxy', 'ctPolycurve', 'ctPolyline'], outer_class=root_module['ON'])
    module.add_enum('cubic_loft_end_condition', ['cubic_loft_ec_quadratic', 'cubic_loft_ec_linear', 'cubic_loft_ec_cubic', 'cubic_loft_ec_natural', 'cubic_loft_ec_unit_tangent', 'cubic_loft_ec_1st_derivative', 'cubic_loft_ec_2nd_derivative', 'cubic_loft_ec_free_cv'], outer_class=root_module['ON'])
    module.add_class('ONX_Model', allow_subclassing=True)
    module.add_class('ONX_Model_Object')
    module.add_class('ONX_Model_RenderLight')
    module.add_class('ONX_Model_UserData')
    module.add_class('ON_2dPoint')
    module.add_class('ON_2dVector')
    module.add_class('ON_3DM_BIG_CHUNK')
    module.add_class('ON_3DM_CHUNK')
    module.add_class('ON_3dPoint')
    module.add_class('ON_3dRay')
    module.add_class('ON_3dVector')
    module.add_class('ON_3dmAnnotationSettings')
    module.add_class('ON_3dmApplication')
    module.add_class('ON_3dmConstructionPlane')
    module.add_class('ON_3dmConstructionPlaneGridDefaults')
    module.add_class('ON_3dmGoo')
    module.add_class('ON_3dmIOSettings')
    module.add_class('ON_3dmNotes')
    module.add_class('ON_3dmPageSettings')
    module.add_class('ON_3dmProperties')
    module.add_class('ON_3dmRenderSettings')
    module.add_class('ON_3dmRevisionHistory')
    module.add_class('ON_3dmSettings')
    module.add_class('ON_3dmUnitsAndTolerances')
    module.add_class('ON_3dmView')
    module.add_class('ON_3dmViewPosition')
    module.add_class('ON_3dmViewTraceImage')
    module.add_class('ON_3dmWallpaperImage')
    module.add_class('ON_4dPoint')
    module.add_class('ON_Base64EncodeStream', allow_subclassing=True)
    module.add_class('ON_BezierCage')
    module.add_class('ON_BezierCurve')
    module.add_class('ON_BezierSurface')
    module.add_class('ON_BinaryArchive', allow_subclassing=True)
    module.add_enum('table_type', ['no_active_table', 'properties_table', 'settings_table', 'bitmap_table', 'texture_mapping_table', 'material_table', 'linetype_table', 'layer_table', 'light_table', 'object_table', 'group_table', 'font_table', 'dimstyle_table', 'hatchpattern_table', 'instance_definition_table', 'historyrecord_table', 'user_table'], outer_class=root_module['ON_BinaryArchive'])
    module.add_class('ON_BinaryArchiveBuffer', parent=root_module['ON_BinaryArchive'])
    module.add_class('ON_BinaryFile', parent=root_module['ON_BinaryArchive'])
    module.add_class('ON_BoundingBox')
    module.add_class('ON_Box')
    module.add_class('ON_BrepRegionTopology')
    module.add_class('ON_BrepTrimPoint')
    module.add_class('ON_Buffer')
    module.add_enum('', ['seek_from_beginning_of_file', 'seek_from_current_position', 'seek_from_end_of_file'], outer_class=root_module['ON_Buffer'])
    module.add_class('ON_BumpFunction')
    module.add_class('ON_COMPONENT_INDEX')
    module.add_enum('TYPE', ['invalid_type', 'brep_vertex', 'brep_edge', 'brep_face', 'brep_trim', 'brep_loop', 'mesh_vertex', 'meshtop_vertex', 'meshtop_edge', 'mesh_face', 'idef_part', 'polycurve_segment', 'pointcloud_point', 'group_member', 'extrusion_bottom_profile', 'extrusion_top_profile', 'extrusion_wall_edge', 'extrusion_wall_surface', 'extrusion_cap_surface', 'extrusion_path', 'dim_linear_point', 'dim_radial_point', 'dim_angular_point', 'dim_ordinate_point', 'dim_text_point', 'no_type'], outer_class=root_module['ON_COMPONENT_INDEX'])
    module.add_class('ON_CheckSum')
    module.add_class('ON_Circle')
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ONX_Model_Object'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ONX_Model_RenderLight'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ONX_Model_UserData'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_3dmConstructionPlane'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_3dmView'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_BrepEdge'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_BrepFace'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_BrepFaceSide'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_BrepLoop'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_BrepRegion'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_BrepTrim'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_BrepVertex'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_CurveProxyHistory'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_DimStyle'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_Font'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_Group'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_HatchLine'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_HatchPattern'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_InstanceDefinition'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_Layer'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_Linetype'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_Localizer'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_MappingRef'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_Material'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_MaterialRef'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_PlugInRef'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_Texture'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_TextureCoordinates'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_TextureMapping'])
    module.add_class('ON_ClassArray', allow_subclassing=True, template_parameters=['ON_UserString'])
    module.add_class('ON_ClassId')
    module.add_class('ON_ClippingPlane')
    module.add_class('ON_ClippingPlaneInfo')
    module.add_class('ON_ClippingRegion')
    module.add_enum('', ['max_clip_plane_count', 'frustum_bitmask', 'near_plane_bitmask', 'far_plane_bitmask', 'clip_plane_bitmask', 'negw_bitmask'], outer_class=root_module['ON_ClippingRegion'])
    module.add_class('ON_Color')
    module.add_class('ON_CompressStream', allow_subclassing=True)
    module.add_class('ON_CompressedBuffer')
    module.add_class('ON_Cone')
    module.add_class('ON_CurveProxyHistory')
    module.add_class('ON_Cylinder')
    module.add_class('ON_DecodeBase64', allow_subclassing=True)
    module.add_class('ON_DisplayMaterialRef')
    module.add_class('ON_EarthAnchorPoint')
    module.add_class('ON_Ellipse')
    module.add_class('ON_Evaluator', allow_subclassing=True)
    module.add_class('ON_FileIterator')
    module.add_class('ON_FileStream')
    module.add_class('ON_FixedSizePool')
    module.add_class('ON_FixedSizePoolIterator')
    module.add_class('ON_HatchLine')
    module.add_class('ON_HatchLoop')
    module.add_enum('eLoopType', ['ltOuter', 'ltInner'], outer_class=root_module['ON_HatchLoop'])
    module.add_class('ON_Interval')
    module.add_class('ON_Line')
    module.add_class('ON_LinetypeSegment')
    module.add_enum('eSegType', ['stLine', 'stSpace'], outer_class=root_module['ON_LinetypeSegment'])
    module.add_class('ON_LocalZero1', allow_subclassing=True)
    module.add_class('ON_Localizer')
    module.add_enum('TYPE', ['no_type', 'sphere_type', 'plane_type', 'cylinder_type', 'curve_type', 'surface_type', 'distance_type', 'force_32bit_localizer_type'], outer_class=root_module['ON_Localizer'])
    module.add_class('ON_MappingChannel')
    module.add_class('ON_MappingRef')
    module.add_class('ON_MappingTag')
    module.add_class('ON_MassProperties')
    module.add_class('ON_MaterialRef')
    module.add_class('ON_Matrix')
    module.add_class('ON_MeshCurvatureStats')
    module.add_class('ON_MeshCurveParameters')
    module.add_class('ON_MeshFace')
    module.add_class('ON_MeshFaceSide')
    module.add_class('ON_MeshNgon')
    module.add_class('ON_MeshNgonList')
    module.add_class('ON_MeshParameters')
    module.add_enum('MESH_STYLE', ['unset_mesh_style', 'render_mesh_fast', 'render_mesh_quality', 'render_mesh_custom', 'render_mesh_per_object'], outer_class=root_module['ON_MeshParameters'])
    module.add_class('ON_MeshPart')
    module.add_class('ON_MeshPartition')
    module.add_class('ON_MeshTopology')
    module.add_class('ON_MeshTopologyEdge')
    module.add_class('ON_MeshTopologyFace')
    module.add_class('ON_MeshTopologyVertex')
    module.add_class('ON_ObjRef')
    module.add_class('ON_ObjRefEvaluationParameter')
    module.add_class('ON_ObjRef_IRefID')
    module.add_class('ON_Object', allow_subclassing=True)
    module.add_class('ON_ObjectArray', template_parameters=['ON_BrepEdge'], parent=root_module['ON_ClassArray< ON_BrepEdge >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_BrepFace'], parent=root_module['ON_ClassArray< ON_BrepFace >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_BrepFaceSide'], parent=root_module['ON_ClassArray< ON_BrepFaceSide >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_BrepLoop'], parent=root_module['ON_ClassArray< ON_BrepLoop >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_BrepRegion'], parent=root_module['ON_ClassArray< ON_BrepRegion >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_BrepTrim'], parent=root_module['ON_ClassArray< ON_BrepTrim >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_BrepVertex'], parent=root_module['ON_ClassArray< ON_BrepVertex >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_DimStyle'], parent=root_module['ON_ClassArray< ON_DimStyle >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_Font'], parent=root_module['ON_ClassArray< ON_Font >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_Group'], parent=root_module['ON_ClassArray< ON_Group >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_HatchPattern'], parent=root_module['ON_ClassArray< ON_HatchPattern >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_InstanceDefinition'], parent=root_module['ON_ClassArray< ON_InstanceDefinition >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_Layer'], parent=root_module['ON_ClassArray< ON_Layer >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_Linetype'], parent=root_module['ON_ClassArray< ON_Linetype >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_Material'], parent=root_module['ON_ClassArray< ON_Material >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_Texture'], parent=root_module['ON_ClassArray< ON_Texture >'])
    module.add_class('ON_ObjectArray', template_parameters=['ON_TextureMapping'], parent=root_module['ON_ClassArray< ON_TextureMapping >'])
    module.add_class('ON_OffsetSurfaceFunction')
    module.add_class('ON_OffsetSurfaceValue')
    module.add_class('ON_Plane')
    module.add_class('ON_PlaneEquation', parent=root_module['ON_3dVector'])
    module.add_class('ON_PlugInRef')
    module.add_class('ON_PolyEdgeHistory')
    module.add_class('ON_PolynomialCurve')
    module.add_class('ON_PolynomialSurface')
    module.add_class('ON_RANDOM_NUMBER_CONTEXT')
    module.add_class('ON_RTree')
    module.add_class('ON_RTreeBBox')
    module.add_class('ON_RTreeBranch')
    module.add_class('ON_RTreeCapsule')
    module.add_class('ON_RTreeIterator')
    module.add_class('ON_RTreeLeaf')
    module.add_class('ON_RTreeMemPool')
    module.add_class('ON_RTreeNode')
    module.add_class('ON_RTreeSearchResult')
    module.add_class('ON_RTreeSphere')
    module.add_class('ON_RandomNumberGenerator')
    module.add_class('ON_Read3dmBufferArchive', parent=root_module['ON_BinaryArchive'])
    module.add_class('ON_RenderingAttributes')
    module.add_class('ON_SSX_EVENT')
    module.add_enum('TYPE', ['no_ssx_event', 'ssx_transverse', 'ssx_tangent', 'ssx_overlap', 'ssx_transverse_point', 'ssx_tangent_point', 'ssx_32bit_enum'], outer_class=root_module['ON_SSX_EVENT'])
    module.add_class('ON_SerialNumberMap')
    module.add_class('MAP_VALUE', outer_class=root_module['ON_SerialNumberMap'])
    module.add_class('SN_ELEMENT', outer_class=root_module['ON_SerialNumberMap'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_2dPoint'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_2dVector'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_2fPoint'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_2fVector'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_3DM_BIG_CHUNK'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_3dPoint'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_3dVector'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_3fPoint'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_3fVector'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_4dPoint'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_4fPoint'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_Bitmap*'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_BrepTrimPoint'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_BumpFunction'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_ClippingPlaneInfo'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_Color'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_Curve*'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_DisplayMaterialRef'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_HatchLoop*'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_HistoryRecord*'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_Interval'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_LinetypeSegment'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_MappingChannel'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_MeshFace'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_MeshPart'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_MeshTopologyEdge'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_MeshTopologyFace'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_MeshTopologyVertex'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_ObjRef_IRefID'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_OffsetSurfaceValue'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_Surface*'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_SurfaceCurvature'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_UUID'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_UuidIndex'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_UuidPair'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['ON_Value*'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['bool'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['double*'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['double'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['int'])
    module.add_class('ON_SimpleArray', allow_subclassing=True, template_parameters=['tagON_2dex'])
    module.add_class('ON_SpaceMorph', allow_subclassing=True)
    module.add_class('ON_Sphere')
    module.add_class('ON_String')
    module.add_class('ON_Sum')
    module.add_class('ON_SurfaceArray', parent=root_module['ON_SimpleArray< ON_Surface* >'])
    module.add_class('ON_SurfaceCurvature')
    module.add_class('ON_SurfaceProperties')
    module.add_class('ON_TensorProduct', allow_subclassing=True)
    module.add_class('ON_TextLog', allow_subclassing=True)
    module.add_class('ON_Texture', parent=root_module['ON_Object'])
    module.add_enum('MAPPING_CHANNEL', ['tc_channel', 'default_channel', 'srfp_channel', 'emap_channel'], outer_class=root_module['ON_Texture'])
    module.add_enum('TYPE', ['no_texture_type', 'bitmap_texture', 'bump_texture', 'transparency_texture', 'emap_texture', 'force_32bit_texture_type'], outer_class=root_module['ON_Texture'])
    module.add_enum('MODE', ['no_texture_mode', 'modulate_texture', 'decal_texture', 'blend_texture', 'force_32bit_texture_mode'], outer_class=root_module['ON_Texture'])
    module.add_enum('FILTER', ['nearest_filter', 'linear_filter', 'force_32bit_texture_filter'], outer_class=root_module['ON_Texture'])
    module.add_enum('WRAP', ['repeat_wrap', 'clamp_wrap', 'force_32bit_texture_wrap'], outer_class=root_module['ON_Texture'])
    module.add_class('ON_TextureCoordinates')
    module.add_class('ON_TextureMapping', parent=root_module['ON_Object'])
    module.add_enum('TYPE', ['no_mapping', 'srfp_mapping', 'plane_mapping', 'cylinder_mapping', 'sphere_mapping', 'box_mapping', 'mesh_mapping_primitive', 'srf_mapping_primitive', 'brep_mapping_primitive', 'force_32bit_mapping_type'], outer_class=root_module['ON_TextureMapping'])
    module.add_enum('PROJECTION', ['no_projection', 'clspt_projection', 'ray_projection', 'force_32bit_mapping_projection'], outer_class=root_module['ON_TextureMapping'])
    module.add_enum('TEXTURE_SPACE', ['single', 'divided', 'force_32bit_texture_space'], outer_class=root_module['ON_TextureMapping'])
    module.add_class('ON_Torus')
    module.add_class('ON_U')
    module.add_class('ON_UUID')
    module.add_class('ON_UncompressStream', allow_subclassing=True)
    module.add_class('ON_UnicodeErrorParameters')
    module.add_class('ON_UnitSystem')
    module.add_class('ON_UserData', parent=root_module['ON_Object'])
    module.add_class('ON_UserDataHolder', parent=root_module['ON_Object'])
    module.add_class('ON_UserString')
    module.add_class('ON_UserStringList', parent=root_module['ON_UserData'])
    module.add_class('ON_UuidIndex')
    module.add_class('ON_UuidIndexList', parent=root_module['ON_SimpleArray< ON_UuidIndex >'])
    module.add_class('ON_UuidList', parent=root_module['ON_SimpleArray< ON_UUID >'])
    module.add_class('ON_UuidPair')
    module.add_class('ON_UuidPairList', parent=root_module['ON_SimpleArray< ON_UuidPair >'])
    module.add_class('ON_WindowsBITMAPINFO')
    module.add_class('ON_WindowsBITMAPINFOHEADER')
    module.add_class('ON_WindowsRGBQUAD')
    module.add_class('ON_Workspace')
    module.add_class('ON_Write3dmBufferArchive', parent=root_module['ON_BinaryArchive'])
    module.add_class('ON_X_EVENT')
    module.add_enum('TYPE', ['no_x_event', 'ccx_point', 'ccx_overlap', 'csx_point', 'csx_overlap'], outer_class=root_module['ON_X_EVENT'])
    module.add_enum('DIRECTION', ['no_x_dir', 'at_end_dir', 'from_above_dir', 'from_below_dir', 'from_on_dir', 'to_above_dir', 'to_below_dir', 'to_on_dir'], outer_class=root_module['ON_X_EVENT'])
    module.add_class('ON_Xform')
    module.add_class('ON_wString')
    module.add_class('tagON_2dex')
    module.add_class('tagON_3dex')
    module.add_class('tagON_4dex')
    module.add_class('tagON_RECT')
    module.add_class('ON_2dPointArray', parent=root_module['ON_SimpleArray< ON_2dPoint >'])
    module.add_class('ON_2dVectorArray', parent=root_module['ON_SimpleArray< ON_2dVector >'])
    module.add_class('ON_2dexMap', parent=root_module['ON_SimpleArray< tagON_2dex >'])
    module.add_class('ON_2fPointArray', parent=root_module['ON_SimpleArray< ON_2fPoint >'])
    module.add_class('ON_2fVectorArray', parent=root_module['ON_SimpleArray< ON_2fVector >'])
    module.add_class('ON_3dPointArray', parent=root_module['ON_SimpleArray< ON_3dPoint >'])
    module.add_class('ON_3dVectorArray', parent=root_module['ON_SimpleArray< ON_3dVector >'])
    module.add_class('ON_3dmObjectAttributes', parent=root_module['ON_Object'])
    module.add_class('ON_3fPointArray', parent=root_module['ON_SimpleArray< ON_3fPoint >'])
    module.add_class('ON_3fVectorArray', parent=root_module['ON_SimpleArray< ON_3fVector >'])
    module.add_class('ON_4dPointArray', parent=root_module['ON_SimpleArray< ON_4dPoint >'])
    module.add_class('ON_4fPointArray', parent=root_module['ON_SimpleArray< ON_4fPoint >'])
    module.add_class('ON_Annotation2Text', parent=root_module['ON_wString'])
    module.add_class('ON_Arc', parent=root_module['ON_Circle'])
    module.add_class('ON_BezierCageMorph', parent=root_module['ON_SpaceMorph'])
    module.add_class('ON_Bitmap', parent=root_module['ON_Object'])
    module.add_class('ON_BrepEdgeArray', parent=root_module['ON_ObjectArray< ON_BrepEdge >'])
    module.add_class('ON_BrepFaceArray', parent=root_module['ON_ObjectArray< ON_BrepFace >'])
    module.add_class('ON_BrepFaceSide', parent=root_module['ON_Object'])
    module.add_class('ON_BrepFaceSideArray', parent=root_module['ON_ObjectArray< ON_BrepFaceSide >'])
    module.add_class('ON_BrepLoopArray', parent=root_module['ON_ObjectArray< ON_BrepLoop >'])
    module.add_class('ON_BrepRegion', parent=root_module['ON_Object'])
    module.add_class('ON_BrepRegionArray', parent=root_module['ON_ObjectArray< ON_BrepRegion >'])
    module.add_class('ON_BrepTrimArray', parent=root_module['ON_ObjectArray< ON_BrepTrim >'])
    module.add_class('ON_BrepVertexArray', parent=root_module['ON_ObjectArray< ON_BrepVertex >'])
    module.add_class('ON_CageMorph', parent=root_module['ON_SpaceMorph'])
    module.add_class('ON_CurveArray', parent=root_module['ON_SimpleArray< ON_Curve* >'])
    module.add_class('ON_DimStyle', parent=root_module['ON_Object'])
    module.add_enum('eArrowType', ['solidtriangle', 'dot', 'tick', 'shorttriangle', 'arrow', 'rectangle', 'longtriangle', 'longertriangle'], outer_class=root_module['ON_DimStyle'])
    module.add_enum('eField', ['fn_name', 'fn_index', 'fn_extextension', 'fn_extoffset', 'fn_arrowsize', 'fn_centermark', 'fn_textgap', 'fn_textheight', 'fn_textalign', 'fn_arrowtype', 'fn_angularunits', 'fn_lengthformat', 'fn_angleformat', 'fn_angleresolution', 'fn_lengthresolution', 'fn_fontindex', 'fn_lengthfactor', 'fn_bAlternate', 'fn_alternate_lengthfactor', 'fn_alternate_lengthformat', 'fn_alternate_lengthresolution', 'fn_alternate_angleformat', 'fn_alternate_angleresolution', 'fn_prefix', 'fn_suffix', 'fn_alternate_prefix', 'fn_alternate_suffix', 'fn_dimextension', 'fn_leaderarrowsize', 'fn_leaderarrowtype', 'fn_suppressextension1', 'fn_suppressextension2', 'fn_last', 'fn_overall_scale', 'fn_ext_line_color_source', 'fn_dim_line_color_source', 'fn_arrow_color_source', 'fn_text_color_source', 'fn_ext_line_color', 'fn_dim_line_color', 'fn_arrow_color', 'fn_text_color', 'fn_ext_line_plot_color_source', 'fn_dim_line_plot_color_source', 'fn_arrow_plot_color_source', 'fn_text_plot_color_source', 'fn_ext_line_plot_color', 'fn_dim_line_plot_color', 'fn_arrow_plot_color', 'fn_text_plot_color', 'fn_ext_line_plot_weight_source', 'fn_dim_line_plot_weight_source', 'fn_ext_line_plot_weight_mm', 'fn_dim_line_plot_weight_mm', 'fn_tolerance_style', 'fn_tolerance_resolution', 'fn_tolerance_upper_value', 'fn_tolerance_lower_value', 'fn_tolerance_height_scale', 'fn_baseline_spacing', 'fn_draw_mask', 'fn_mask_color_source', 'fn_mask_color', 'fn_mask_border', 'fn_dimscale', 'fn_dimscale_source', 'fn_really_last'], outer_class=root_module['ON_DimStyle'])
    module.add_class('ON_DimensionExtra', parent=root_module['ON_UserData'])
    module.add_class('ON_DocumentUserStringList', parent=root_module['ON_Object'])
    module.add_class('ON_EmbeddedBitmap', parent=root_module['ON_Bitmap'])
    module.add_class('ON_EmbeddedFile', parent=root_module['ON_Object'])
    module.add_class('ON_Font', parent=root_module['ON_Object'])
    module.add_enum('', ['face_name_size', 'bold_weight', 'medium_weight', 'normal_weight', 'light_weight', 'default_charset', 'symbol_charset', 'normal_font_height'], outer_class=root_module['ON_Font'])
    module.add_class('ON_Geometry', parent=root_module['ON_Object'])
    module.add_class('ON_Group', parent=root_module['ON_Object'])
    module.add_class('ON_Hatch', parent=root_module['ON_Geometry'])
    module.add_class('ON_HatchPattern', parent=root_module['ON_Object'])
    module.add_enum('eFillType', ['ftSolid', 'ftLines', 'ftGradient', 'ftLast'], outer_class=root_module['ON_HatchPattern'])
    module.add_class('ON_HistoryRecord', parent=root_module['ON_Object'])
    module.add_enum('RECORD_TYPE', ['history_parameters', 'feature_parameters', 'force_32bit_record_type'], outer_class=root_module['ON_HistoryRecord'])
    module.add_class('ON_InstanceDefinition', parent=root_module['ON_Geometry'])
    module.add_enum('IDEF_UPDATE_TYPE', ['static_def', 'embedded_def', 'linked_and_embedded_def', 'linked_def', 'force_32bit_idef_update_type'], outer_class=root_module['ON_InstanceDefinition'])
    module.add_enum('', ['no_idef_settings', 'idef_name_setting', 'idef_description_setting', 'idef_url_setting', 'idef_units_setting', 'idef_source_archive_setting', 'idef_userdata_setting', 'all_idef_settings'], outer_class=root_module['ON_InstanceDefinition'])
    module.add_class('ON_InstanceRef', parent=root_module['ON_Geometry'])
    module.add_class('ON_Layer', parent=root_module['ON_Object'])
    module.add_enum('PER_VIEWPORT_SETTINGS', ['per_viewport_none', 'per_viewport_id', 'per_viewport_color', 'per_viewport_plot_color', 'per_viewport_plot_weight', 'per_viewport_visible', 'per_viewport_persistent_visibility', 'per_viewport_all_settings'], outer_class=root_module['ON_Layer'])
    module.add_enum('LAYER_SETTINGS', ['no_layer_settings', 'userdata_settings', 'color_settings', 'plot_color_settings', 'plot_weight_settings', 'visible_settings', 'locked_settings', 'all_layer_settings'], outer_class=root_module['ON_Layer'])
    module.add_class('ON_Light', parent=root_module['ON_Geometry'])
    module.add_class('ON_Linetype', parent=root_module['ON_Object'])
    module.add_class('ON_Material', parent=root_module['ON_Object'])
    module.add_class('ON_Mesh', parent=root_module['ON_Geometry'])
    module.add_class('ON_MeshEdgeRef', parent=root_module['ON_Geometry'])
    module.add_class('ON_MeshFaceRef', parent=root_module['ON_Geometry'])
    module.add_class('ON_MeshVertexRef', parent=root_module['ON_Geometry'])
    module.add_class('ON_MorphControl', parent=root_module['ON_Geometry'])
    module.add_class('ON_NurbsCage', parent=root_module['ON_Geometry'])
    module.add_class('ON_ObjectRenderingAttributes', parent=root_module['ON_RenderingAttributes'])
    module.add_class('ON_Point', parent=root_module['ON_Geometry'])
    module.add_class('ON_PointCloud', parent=root_module['ON_Geometry'])
    module.add_class('ON_PointGrid', parent=root_module['ON_Geometry'])
    module.add_class('ON_Polyline', parent=root_module['ON_3dPointArray'])
    module.add_class('ON_Surface', parent=root_module['ON_Geometry'])
    module.add_enum('ISO', ['not_iso', 'x_iso', 'y_iso', 'W_iso', 'S_iso', 'E_iso', 'N_iso', 'iso_count'], outer_class=root_module['ON_Surface'])
    module.add_class('ON_SurfaceProxy', parent=root_module['ON_Surface'])
    module.add_class('ON_TextDot', parent=root_module['ON_Geometry'])
    module.add_class('ON_TextExtra', parent=root_module['ON_UserData'])
    module.add_class('ON_UnknownUserData', parent=root_module['ON_UserData'])
    module.add_class('ON_Viewport', parent=root_module['ON_Geometry'])
    module.add_class('ON_WindowsBitmap', parent=root_module['ON_Bitmap'])
    module.add_class('ON_WindowsBitmapEx', parent=root_module['ON_WindowsBitmap'])
    module.add_class('ON_Annotation', parent=root_module['ON_Geometry'])
    module.add_enum('SYMBOLS', ['degreesym', 'radiussym', 'diametersym', 'plusminussym'], outer_class=root_module['ON_Annotation'])
    module.add_class('ON_Annotation2', parent=root_module['ON_Geometry'])
    module.add_enum('SYMBOLS', ['degreesym', 'radiussym', 'diametersym', 'plusminussym'], outer_class=root_module['ON_Annotation2'])
    module.add_enum('eTextJustification', ['tjUndefined', 'tjLeft', 'tjCenter', 'tjRight', 'tjBottom', 'tjMiddle', 'tjTop', 'tjBottomLeft', 'tjBottomCenter', 'tjBottomRight', 'tjMiddleLeft', 'tjMiddleCenter', 'tjMiddleRight', 'tjTopLeft', 'tjTopCenter', 'tjTopRight'], outer_class=root_module['ON_Annotation2'])
    module.add_class('ON_AnnotationArrow', parent=root_module['ON_Geometry'])
    module.add_class('ON_AnnotationTextDot', parent=root_module['ON_Point'])
    module.add_class('ON_Brep', parent=root_module['ON_Geometry'])
    module.add_class('ON_BrepFace', parent=root_module['ON_SurfaceProxy'])
    module.add_class('ON_BrepLoop', parent=root_module['ON_Geometry'])
    module.add_enum('TYPE', ['unknown', 'outer', 'inner', 'slit', 'crvonsrf', 'ptonsrf', 'type_count'], outer_class=root_module['ON_BrepLoop'])
    module.add_class('ON_BrepVertex', parent=root_module['ON_Point'])
    module.add_class('ON_Curve', parent=root_module['ON_Geometry'])
    module.add_class('ON_CurveOnSurface', parent=root_module['ON_Curve'])
    module.add_class('ON_CurveProxy', parent=root_module['ON_Curve'])
    module.add_class('ON_DetailView', parent=root_module['ON_Geometry'])
    module.add_class('ON_Extrusion', parent=root_module['ON_Surface'])
    module.add_class('ON_Leader', parent=root_module['ON_Annotation'])
    module.add_class('ON_Leader2', parent=root_module['ON_Annotation2'])
    module.add_enum('POINT_INDEX', ['arrow_pt_index', 'text_pivot_pt', 'tail_pt'], outer_class=root_module['ON_Leader2'])
    module.add_class('ON_LineCurve', parent=root_module['ON_Curve'])
    module.add_class('ON_LinearDimension', parent=root_module['ON_Annotation'])
    module.add_class('ON_LinearDimension2', parent=root_module['ON_Annotation2'])
    module.add_enum('POINT_INDEX', ['ext0_pt_index', 'arrow0_pt_index', 'ext1_pt_index', 'arrow1_pt_index', 'userpositionedtext_pt_index', 'dim_pt_count', 'text_pivot_pt', 'dim_mid_pt'], outer_class=root_module['ON_LinearDimension2'])
    module.add_class('ON_NurbsCurve', parent=root_module['ON_Curve'])
    module.add_class('ON_NurbsSurface', parent=root_module['ON_Surface'])
    module.add_class('ON_OffsetSurface', parent=root_module['ON_SurfaceProxy'])
    module.add_class('ON_OrdinateDimension2', parent=root_module['ON_Annotation2'])
    module.add_enum('POINT_INDEX', ['definition_pt_index', 'leader_end_pt_index', 'dim_pt_count', 'text_pivot_pt', 'offset_pt_0', 'offset_pt_1'], outer_class=root_module['ON_OrdinateDimension2'])
    module.add_enum('DIRECTION', ['x', 'y'], outer_class=root_module['ON_OrdinateDimension2'])
    module.add_class('ON_PlaneSurface', parent=root_module['ON_Surface'])
    module.add_class('ON_PolyCurve', parent=root_module['ON_Curve'])
    module.add_class('ON_PolylineCurve', parent=root_module['ON_Curve'])
    module.add_class('ON_RadialDimension', parent=root_module['ON_Annotation'])
    module.add_class('ON_RadialDimension2', parent=root_module['ON_Annotation2'])
    module.add_enum('POINT_INDEX', ['center_pt_index', 'arrow_pt_index', 'tail_pt_index', 'knee_pt_index', 'dim_pt_count', 'text_pivot_pt'], outer_class=root_module['ON_RadialDimension2'])
    module.add_class('ON_RevSurface', parent=root_module['ON_Surface'])
    module.add_class('ON_SumSurface', parent=root_module['ON_Surface'])
    module.add_class('ON_TextEntity', parent=root_module['ON_Annotation'])
    module.add_class('ON_TextEntity2', parent=root_module['ON_Annotation2'])
    module.add_class('ON_AngularDimension', parent=root_module['ON_Annotation'])
    module.add_class('ON_AngularDimension2', parent=root_module['ON_Annotation2'])
    module.add_enum('POINT_INDEX', ['userpositionedtext_pt_index', 'start_pt_index', 'end_pt_index', 'arc_pt_index', 'dim_pt_count', 'text_pivot_pt', 'arcstart_pt', 'arcend_pt', 'arcmid_pt', 'arccenter_pt', 'extension0_pt', 'extension1_pt'], outer_class=root_module['ON_AngularDimension2'])
    module.add_class('ON_ArcCurve', parent=root_module['ON_Curve'])
    module.add_class('ON_BrepEdge', parent=root_module['ON_CurveProxy'])
    module.add_class('ON_BrepTrim', parent=root_module['ON_CurveProxy'])
    module.add_enum('TYPE', ['unknown', 'boundary', 'mated', 'seam', 'singular', 'crvonsrf', 'ptonsrf', 'slit', 'trim_type_count', 'force_32_bit_trim_type'], outer_class=root_module['ON_BrepTrim'])
    module.add_class('ON_ClippingPlaneSurface', parent=root_module['ON_PlaneSurface'])
    typehandlers.add_type_alias(u'bool ( * ) ( ON_BrepFace const *, ON_3dPoint const *, ON_3dPoint & ) *', u'TEXMAP_BREP_FACE_CLOSEST_POINT')
    typehandlers.add_type_alias(u'bool ( * ) ( ON_BrepFace const *, ON_3dPoint const *, ON_3dPoint & ) **', u'TEXMAP_BREP_FACE_CLOSEST_POINT*')
    typehandlers.add_type_alias(u'bool ( * ) ( ON_BrepFace const *, ON_3dPoint const *, ON_3dPoint & ) *&', u'TEXMAP_BREP_FACE_CLOSEST_POINT&')
    typehandlers.add_type_alias(u'tagON_2dex', u'ON_2dex')
    typehandlers.add_type_alias(u'tagON_2dex*', u'ON_2dex*')
    typehandlers.add_type_alias(u'tagON_2dex&', u'ON_2dex&')
    module.add_typedef(root_module['tagON_2dex'], 'ON_2dex')
    typehandlers.add_type_alias(u'tagON_3dex', u'ON_3dex')
    typehandlers.add_type_alias(u'tagON_3dex*', u'ON_3dex*')
    typehandlers.add_type_alias(u'tagON_3dex&', u'ON_3dex&')
    module.add_typedef(root_module['tagON_3dex'], 'ON_3dex')
    typehandlers.add_type_alias(u'int ( * ) ( ON_Line const *, ON_BrepFace const *, ON_SimpleArray< ON_X_EVENT > & ) *', u'TEXMAP_INTERSECT_LINE_SURFACE')
    typehandlers.add_type_alias(u'int ( * ) ( ON_Line const *, ON_BrepFace const *, ON_SimpleArray< ON_X_EVENT > & ) **', u'TEXMAP_INTERSECT_LINE_SURFACE*')
    typehandlers.add_type_alias(u'int ( * ) ( ON_Line const *, ON_BrepFace const *, ON_SimpleArray< ON_X_EVENT > & ) *&', u'TEXMAP_INTERSECT_LINE_SURFACE&')
    typehandlers.add_type_alias(u'unsigned char', u'ON__UINT8')
    typehandlers.add_type_alias(u'unsigned char*', u'ON__UINT8*')
    typehandlers.add_type_alias(u'unsigned char&', u'ON__UINT8&')
    typehandlers.add_type_alias(u'int', u'ON_BOOL32')
    typehandlers.add_type_alias(u'int*', u'ON_BOOL32*')
    typehandlers.add_type_alias(u'int&', u'ON_BOOL32&')
    typehandlers.add_type_alias(u'short int', u'ON__INT16')
    typehandlers.add_type_alias(u'short int*', u'ON__INT16*')
    typehandlers.add_type_alias(u'short int&', u'ON__INT16&')
    typehandlers.add_type_alias(u'int', u'ON__INT32')
    typehandlers.add_type_alias(u'int*', u'ON__INT32*')
    typehandlers.add_type_alias(u'int&', u'ON__INT32&')
    typehandlers.add_type_alias(u'long long int', u'ON__INT64')
    typehandlers.add_type_alias(u'long long int*', u'ON__INT64*')
    typehandlers.add_type_alias(u'long long int&', u'ON__INT64&')
    typehandlers.add_type_alias(u'tagON_4dex', u'ON_4dex')
    typehandlers.add_type_alias(u'tagON_4dex*', u'ON_4dex*')
    typehandlers.add_type_alias(u'tagON_4dex&', u'ON_4dex&')
    module.add_typedef(root_module['tagON_4dex'], 'ON_4dex')
    typehandlers.add_type_alias(u'void ( * ) ( ON_Buffer * ) *', u'ON_Buffer_ErrorHandler')
    typehandlers.add_type_alias(u'void ( * ) ( ON_Buffer * ) **', u'ON_Buffer_ErrorHandler*')
    typehandlers.add_type_alias(u'void ( * ) ( ON_Buffer * ) *&', u'ON_Buffer_ErrorHandler&')
    typehandlers.add_type_alias(u'tagON_RECT', u'ON_RECT')
    typehandlers.add_type_alias(u'tagON_RECT*', u'ON_RECT*')
    typehandlers.add_type_alias(u'tagON_RECT&', u'ON_RECT&')
    module.add_typedef(root_module['tagON_RECT'], 'ON_RECT')
    typehandlers.add_type_alias(u'unsigned int', u'ON__UINT_PTR')
    typehandlers.add_type_alias(u'unsigned int*', u'ON__UINT_PTR*')
    typehandlers.add_type_alias(u'unsigned int&', u'ON__UINT_PTR&')
    typehandlers.add_type_alias(u'bool ( * ) ( void *, ON__UINT32, void const * ) *', u'ON_StreamCallbackFunction')
    typehandlers.add_type_alias(u'bool ( * ) ( void *, ON__UINT32, void const * ) **', u'ON_StreamCallbackFunction*')
    typehandlers.add_type_alias(u'bool ( * ) ( void *, ON__UINT32, void const * ) *&', u'ON_StreamCallbackFunction&')
    typehandlers.add_type_alias(u'short unsigned int', u'ON__UINT16')
    typehandlers.add_type_alias(u'short unsigned int*', u'ON__UINT16*')
    typehandlers.add_type_alias(u'short unsigned int&', u'ON__UINT16&')
    typehandlers.add_type_alias(u'unsigned int', u'ON__UINT32')
    typehandlers.add_type_alias(u'unsigned int*', u'ON__UINT32*')
    typehandlers.add_type_alias(u'unsigned int&', u'ON__UINT32&')
    typehandlers.add_type_alias(u'long long unsigned int', u'ON__UINT64')
    typehandlers.add_type_alias(u'long long unsigned int*', u'ON__UINT64*')
    typehandlers.add_type_alias(u'long long unsigned int&', u'ON__UINT64&')
    typehandlers.add_type_alias(u'int', u'ON__INT_PTR')
    typehandlers.add_type_alias(u'int*', u'ON__INT_PTR*')
    typehandlers.add_type_alias(u'int&', u'ON__INT_PTR&')
    typehandlers.add_type_alias(u'char', u'ON__INT8')
    typehandlers.add_type_alias(u'char*', u'ON__INT8*')
    typehandlers.add_type_alias(u'char&', u'ON__INT8&')
    
    ## Register a nested module for the namespace std
    
    nested_module = module.add_cpp_namespace('std')
    register_types_std(nested_module)
    

def register_types_std(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    register_ON_methods(root_module, root_module['ON'])
    register_ONX_Model_methods(root_module, root_module['ONX_Model'])
    register_ONX_Model_Object_methods(root_module, root_module['ONX_Model_Object'])
    register_ONX_Model_RenderLight_methods(root_module, root_module['ONX_Model_RenderLight'])
    register_ONX_Model_UserData_methods(root_module, root_module['ONX_Model_UserData'])
    register_ON_2dPoint_methods(root_module, root_module['ON_2dPoint'])
    register_ON_2dVector_methods(root_module, root_module['ON_2dVector'])
    register_ON_3DM_BIG_CHUNK_methods(root_module, root_module['ON_3DM_BIG_CHUNK'])
    register_ON_3DM_CHUNK_methods(root_module, root_module['ON_3DM_CHUNK'])
    register_ON_3dPoint_methods(root_module, root_module['ON_3dPoint'])
    register_ON_3dRay_methods(root_module, root_module['ON_3dRay'])
    register_ON_3dVector_methods(root_module, root_module['ON_3dVector'])
    register_ON_3dmAnnotationSettings_methods(root_module, root_module['ON_3dmAnnotationSettings'])
    register_ON_3dmApplication_methods(root_module, root_module['ON_3dmApplication'])
    register_ON_3dmConstructionPlane_methods(root_module, root_module['ON_3dmConstructionPlane'])
    register_ON_3dmConstructionPlaneGridDefaults_methods(root_module, root_module['ON_3dmConstructionPlaneGridDefaults'])
    register_ON_3dmGoo_methods(root_module, root_module['ON_3dmGoo'])
    register_ON_3dmIOSettings_methods(root_module, root_module['ON_3dmIOSettings'])
    register_ON_3dmNotes_methods(root_module, root_module['ON_3dmNotes'])
    register_ON_3dmPageSettings_methods(root_module, root_module['ON_3dmPageSettings'])
    register_ON_3dmProperties_methods(root_module, root_module['ON_3dmProperties'])
    register_ON_3dmRenderSettings_methods(root_module, root_module['ON_3dmRenderSettings'])
    register_ON_3dmRevisionHistory_methods(root_module, root_module['ON_3dmRevisionHistory'])
    register_ON_3dmSettings_methods(root_module, root_module['ON_3dmSettings'])
    register_ON_3dmUnitsAndTolerances_methods(root_module, root_module['ON_3dmUnitsAndTolerances'])
    register_ON_3dmView_methods(root_module, root_module['ON_3dmView'])
    register_ON_3dmViewPosition_methods(root_module, root_module['ON_3dmViewPosition'])
    register_ON_3dmViewTraceImage_methods(root_module, root_module['ON_3dmViewTraceImage'])
    register_ON_3dmWallpaperImage_methods(root_module, root_module['ON_3dmWallpaperImage'])
    register_ON_4dPoint_methods(root_module, root_module['ON_4dPoint'])
    register_ON_Base64EncodeStream_methods(root_module, root_module['ON_Base64EncodeStream'])
    register_ON_BezierCage_methods(root_module, root_module['ON_BezierCage'])
    register_ON_BezierCurve_methods(root_module, root_module['ON_BezierCurve'])
    register_ON_BezierSurface_methods(root_module, root_module['ON_BezierSurface'])
    register_ON_BinaryArchive_methods(root_module, root_module['ON_BinaryArchive'])
    register_ON_BinaryArchiveBuffer_methods(root_module, root_module['ON_BinaryArchiveBuffer'])
    register_ON_BinaryFile_methods(root_module, root_module['ON_BinaryFile'])
    register_ON_BoundingBox_methods(root_module, root_module['ON_BoundingBox'])
    register_ON_Box_methods(root_module, root_module['ON_Box'])
    register_ON_BrepRegionTopology_methods(root_module, root_module['ON_BrepRegionTopology'])
    register_ON_BrepTrimPoint_methods(root_module, root_module['ON_BrepTrimPoint'])
    register_ON_Buffer_methods(root_module, root_module['ON_Buffer'])
    register_ON_BumpFunction_methods(root_module, root_module['ON_BumpFunction'])
    register_ON_COMPONENT_INDEX_methods(root_module, root_module['ON_COMPONENT_INDEX'])
    register_ON_CheckSum_methods(root_module, root_module['ON_CheckSum'])
    register_ON_Circle_methods(root_module, root_module['ON_Circle'])
    register_ON_ClassArray__ONX_Model_Object_methods(root_module, root_module['ON_ClassArray< ONX_Model_Object >'])
    register_ON_ClassArray__ONX_Model_RenderLight_methods(root_module, root_module['ON_ClassArray< ONX_Model_RenderLight >'])
    register_ON_ClassArray__ONX_Model_UserData_methods(root_module, root_module['ON_ClassArray< ONX_Model_UserData >'])
    register_ON_ClassArray__ON_3dmConstructionPlane_methods(root_module, root_module['ON_ClassArray< ON_3dmConstructionPlane >'])
    register_ON_ClassArray__ON_3dmView_methods(root_module, root_module['ON_ClassArray< ON_3dmView >'])
    register_ON_ClassArray__ON_BrepEdge_methods(root_module, root_module['ON_ClassArray< ON_BrepEdge >'])
    register_ON_ClassArray__ON_BrepFace_methods(root_module, root_module['ON_ClassArray< ON_BrepFace >'])
    register_ON_ClassArray__ON_BrepFaceSide_methods(root_module, root_module['ON_ClassArray< ON_BrepFaceSide >'])
    register_ON_ClassArray__ON_BrepLoop_methods(root_module, root_module['ON_ClassArray< ON_BrepLoop >'])
    register_ON_ClassArray__ON_BrepRegion_methods(root_module, root_module['ON_ClassArray< ON_BrepRegion >'])
    register_ON_ClassArray__ON_BrepTrim_methods(root_module, root_module['ON_ClassArray< ON_BrepTrim >'])
    register_ON_ClassArray__ON_BrepVertex_methods(root_module, root_module['ON_ClassArray< ON_BrepVertex >'])
    register_ON_ClassArray__ON_CurveProxyHistory_methods(root_module, root_module['ON_ClassArray< ON_CurveProxyHistory >'])
    register_ON_ClassArray__ON_DimStyle_methods(root_module, root_module['ON_ClassArray< ON_DimStyle >'])
    register_ON_ClassArray__ON_Font_methods(root_module, root_module['ON_ClassArray< ON_Font >'])
    register_ON_ClassArray__ON_Group_methods(root_module, root_module['ON_ClassArray< ON_Group >'])
    register_ON_ClassArray__ON_HatchLine_methods(root_module, root_module['ON_ClassArray< ON_HatchLine >'])
    register_ON_ClassArray__ON_HatchPattern_methods(root_module, root_module['ON_ClassArray< ON_HatchPattern >'])
    register_ON_ClassArray__ON_InstanceDefinition_methods(root_module, root_module['ON_ClassArray< ON_InstanceDefinition >'])
    register_ON_ClassArray__ON_Layer_methods(root_module, root_module['ON_ClassArray< ON_Layer >'])
    register_ON_ClassArray__ON_Linetype_methods(root_module, root_module['ON_ClassArray< ON_Linetype >'])
    register_ON_ClassArray__ON_Localizer_methods(root_module, root_module['ON_ClassArray< ON_Localizer >'])
    register_ON_ClassArray__ON_MappingRef_methods(root_module, root_module['ON_ClassArray< ON_MappingRef >'])
    register_ON_ClassArray__ON_Material_methods(root_module, root_module['ON_ClassArray< ON_Material >'])
    register_ON_ClassArray__ON_MaterialRef_methods(root_module, root_module['ON_ClassArray< ON_MaterialRef >'])
    register_ON_ClassArray__ON_PlugInRef_methods(root_module, root_module['ON_ClassArray< ON_PlugInRef >'])
    register_ON_ClassArray__ON_Texture_methods(root_module, root_module['ON_ClassArray< ON_Texture >'])
    register_ON_ClassArray__ON_TextureCoordinates_methods(root_module, root_module['ON_ClassArray< ON_TextureCoordinates >'])
    register_ON_ClassArray__ON_TextureMapping_methods(root_module, root_module['ON_ClassArray< ON_TextureMapping >'])
    register_ON_ClassArray__ON_UserString_methods(root_module, root_module['ON_ClassArray< ON_UserString >'])
    register_ON_ClassId_methods(root_module, root_module['ON_ClassId'])
    register_ON_ClippingPlane_methods(root_module, root_module['ON_ClippingPlane'])
    register_ON_ClippingPlaneInfo_methods(root_module, root_module['ON_ClippingPlaneInfo'])
    register_ON_ClippingRegion_methods(root_module, root_module['ON_ClippingRegion'])
    register_ON_Color_methods(root_module, root_module['ON_Color'])
    register_ON_CompressStream_methods(root_module, root_module['ON_CompressStream'])
    register_ON_CompressedBuffer_methods(root_module, root_module['ON_CompressedBuffer'])
    register_ON_Cone_methods(root_module, root_module['ON_Cone'])
    register_ON_CurveProxyHistory_methods(root_module, root_module['ON_CurveProxyHistory'])
    register_ON_Cylinder_methods(root_module, root_module['ON_Cylinder'])
    register_ON_DecodeBase64_methods(root_module, root_module['ON_DecodeBase64'])
    register_ON_DisplayMaterialRef_methods(root_module, root_module['ON_DisplayMaterialRef'])
    register_ON_EarthAnchorPoint_methods(root_module, root_module['ON_EarthAnchorPoint'])
    register_ON_Ellipse_methods(root_module, root_module['ON_Ellipse'])
    register_ON_Evaluator_methods(root_module, root_module['ON_Evaluator'])
    register_ON_FileIterator_methods(root_module, root_module['ON_FileIterator'])
    register_ON_FileStream_methods(root_module, root_module['ON_FileStream'])
    register_ON_FixedSizePool_methods(root_module, root_module['ON_FixedSizePool'])
    register_ON_FixedSizePoolIterator_methods(root_module, root_module['ON_FixedSizePoolIterator'])
    register_ON_HatchLine_methods(root_module, root_module['ON_HatchLine'])
    register_ON_HatchLoop_methods(root_module, root_module['ON_HatchLoop'])
    register_ON_Interval_methods(root_module, root_module['ON_Interval'])
    register_ON_Line_methods(root_module, root_module['ON_Line'])
    register_ON_LinetypeSegment_methods(root_module, root_module['ON_LinetypeSegment'])
    register_ON_LocalZero1_methods(root_module, root_module['ON_LocalZero1'])
    register_ON_Localizer_methods(root_module, root_module['ON_Localizer'])
    register_ON_MappingChannel_methods(root_module, root_module['ON_MappingChannel'])
    register_ON_MappingRef_methods(root_module, root_module['ON_MappingRef'])
    register_ON_MappingTag_methods(root_module, root_module['ON_MappingTag'])
    register_ON_MassProperties_methods(root_module, root_module['ON_MassProperties'])
    register_ON_MaterialRef_methods(root_module, root_module['ON_MaterialRef'])
    register_ON_Matrix_methods(root_module, root_module['ON_Matrix'])
    register_ON_MeshCurvatureStats_methods(root_module, root_module['ON_MeshCurvatureStats'])
    register_ON_MeshCurveParameters_methods(root_module, root_module['ON_MeshCurveParameters'])
    register_ON_MeshFace_methods(root_module, root_module['ON_MeshFace'])
    register_ON_MeshFaceSide_methods(root_module, root_module['ON_MeshFaceSide'])
    register_ON_MeshNgon_methods(root_module, root_module['ON_MeshNgon'])
    register_ON_MeshNgonList_methods(root_module, root_module['ON_MeshNgonList'])
    register_ON_MeshParameters_methods(root_module, root_module['ON_MeshParameters'])
    register_ON_MeshPart_methods(root_module, root_module['ON_MeshPart'])
    register_ON_MeshPartition_methods(root_module, root_module['ON_MeshPartition'])
    register_ON_MeshTopology_methods(root_module, root_module['ON_MeshTopology'])
    register_ON_MeshTopologyEdge_methods(root_module, root_module['ON_MeshTopologyEdge'])
    register_ON_MeshTopologyFace_methods(root_module, root_module['ON_MeshTopologyFace'])
    register_ON_MeshTopologyVertex_methods(root_module, root_module['ON_MeshTopologyVertex'])
    register_ON_ObjRef_methods(root_module, root_module['ON_ObjRef'])
    register_ON_ObjRefEvaluationParameter_methods(root_module, root_module['ON_ObjRefEvaluationParameter'])
    register_ON_ObjRef_IRefID_methods(root_module, root_module['ON_ObjRef_IRefID'])
    register_ON_Object_methods(root_module, root_module['ON_Object'])
    register_ON_ObjectArray__ON_BrepEdge_methods(root_module, root_module['ON_ObjectArray< ON_BrepEdge >'])
    register_ON_ObjectArray__ON_BrepFace_methods(root_module, root_module['ON_ObjectArray< ON_BrepFace >'])
    register_ON_ObjectArray__ON_BrepFaceSide_methods(root_module, root_module['ON_ObjectArray< ON_BrepFaceSide >'])
    register_ON_ObjectArray__ON_BrepLoop_methods(root_module, root_module['ON_ObjectArray< ON_BrepLoop >'])
    register_ON_ObjectArray__ON_BrepRegion_methods(root_module, root_module['ON_ObjectArray< ON_BrepRegion >'])
    register_ON_ObjectArray__ON_BrepTrim_methods(root_module, root_module['ON_ObjectArray< ON_BrepTrim >'])
    register_ON_ObjectArray__ON_BrepVertex_methods(root_module, root_module['ON_ObjectArray< ON_BrepVertex >'])
    register_ON_ObjectArray__ON_DimStyle_methods(root_module, root_module['ON_ObjectArray< ON_DimStyle >'])
    register_ON_ObjectArray__ON_Font_methods(root_module, root_module['ON_ObjectArray< ON_Font >'])
    register_ON_ObjectArray__ON_Group_methods(root_module, root_module['ON_ObjectArray< ON_Group >'])
    register_ON_ObjectArray__ON_HatchPattern_methods(root_module, root_module['ON_ObjectArray< ON_HatchPattern >'])
    register_ON_ObjectArray__ON_InstanceDefinition_methods(root_module, root_module['ON_ObjectArray< ON_InstanceDefinition >'])
    register_ON_ObjectArray__ON_Layer_methods(root_module, root_module['ON_ObjectArray< ON_Layer >'])
    register_ON_ObjectArray__ON_Linetype_methods(root_module, root_module['ON_ObjectArray< ON_Linetype >'])
    register_ON_ObjectArray__ON_Material_methods(root_module, root_module['ON_ObjectArray< ON_Material >'])
    register_ON_ObjectArray__ON_Texture_methods(root_module, root_module['ON_ObjectArray< ON_Texture >'])
    register_ON_ObjectArray__ON_TextureMapping_methods(root_module, root_module['ON_ObjectArray< ON_TextureMapping >'])
    register_ON_OffsetSurfaceFunction_methods(root_module, root_module['ON_OffsetSurfaceFunction'])
    register_ON_OffsetSurfaceValue_methods(root_module, root_module['ON_OffsetSurfaceValue'])
    register_ON_Plane_methods(root_module, root_module['ON_Plane'])
    register_ON_PlaneEquation_methods(root_module, root_module['ON_PlaneEquation'])
    register_ON_PlugInRef_methods(root_module, root_module['ON_PlugInRef'])
    register_ON_PolyEdgeHistory_methods(root_module, root_module['ON_PolyEdgeHistory'])
    register_ON_PolynomialCurve_methods(root_module, root_module['ON_PolynomialCurve'])
    register_ON_PolynomialSurface_methods(root_module, root_module['ON_PolynomialSurface'])
    register_ON_RANDOM_NUMBER_CONTEXT_methods(root_module, root_module['ON_RANDOM_NUMBER_CONTEXT'])
    register_ON_RTree_methods(root_module, root_module['ON_RTree'])
    register_ON_RTreeBBox_methods(root_module, root_module['ON_RTreeBBox'])
    register_ON_RTreeBranch_methods(root_module, root_module['ON_RTreeBranch'])
    register_ON_RTreeCapsule_methods(root_module, root_module['ON_RTreeCapsule'])
    register_ON_RTreeIterator_methods(root_module, root_module['ON_RTreeIterator'])
    register_ON_RTreeLeaf_methods(root_module, root_module['ON_RTreeLeaf'])
    register_ON_RTreeMemPool_methods(root_module, root_module['ON_RTreeMemPool'])
    register_ON_RTreeNode_methods(root_module, root_module['ON_RTreeNode'])
    register_ON_RTreeSearchResult_methods(root_module, root_module['ON_RTreeSearchResult'])
    register_ON_RTreeSphere_methods(root_module, root_module['ON_RTreeSphere'])
    register_ON_RandomNumberGenerator_methods(root_module, root_module['ON_RandomNumberGenerator'])
    register_ON_Read3dmBufferArchive_methods(root_module, root_module['ON_Read3dmBufferArchive'])
    register_ON_RenderingAttributes_methods(root_module, root_module['ON_RenderingAttributes'])
    register_ON_SSX_EVENT_methods(root_module, root_module['ON_SSX_EVENT'])
    register_ON_SerialNumberMap_methods(root_module, root_module['ON_SerialNumberMap'])
    register_ON_SerialNumberMapMAP_VALUE_methods(root_module, root_module['ON_SerialNumberMap::MAP_VALUE'])
    register_ON_SerialNumberMapSN_ELEMENT_methods(root_module, root_module['ON_SerialNumberMap::SN_ELEMENT'])
    register_ON_SimpleArray__ON_2dPoint_methods(root_module, root_module['ON_SimpleArray< ON_2dPoint >'])
    register_ON_SimpleArray__ON_2dVector_methods(root_module, root_module['ON_SimpleArray< ON_2dVector >'])
    register_ON_SimpleArray__ON_2fPoint_methods(root_module, root_module['ON_SimpleArray< ON_2fPoint >'])
    register_ON_SimpleArray__ON_2fVector_methods(root_module, root_module['ON_SimpleArray< ON_2fVector >'])
    register_ON_SimpleArray__ON_3DM_BIG_CHUNK_methods(root_module, root_module['ON_SimpleArray< ON_3DM_BIG_CHUNK >'])
    register_ON_SimpleArray__ON_3dPoint_methods(root_module, root_module['ON_SimpleArray< ON_3dPoint >'])
    register_ON_SimpleArray__ON_3dVector_methods(root_module, root_module['ON_SimpleArray< ON_3dVector >'])
    register_ON_SimpleArray__ON_3fPoint_methods(root_module, root_module['ON_SimpleArray< ON_3fPoint >'])
    register_ON_SimpleArray__ON_3fVector_methods(root_module, root_module['ON_SimpleArray< ON_3fVector >'])
    register_ON_SimpleArray__ON_4dPoint_methods(root_module, root_module['ON_SimpleArray< ON_4dPoint >'])
    register_ON_SimpleArray__ON_4fPoint_methods(root_module, root_module['ON_SimpleArray< ON_4fPoint >'])
    register_ON_SimpleArray__ON_Bitmap__star___methods(root_module, root_module['ON_SimpleArray< ON_Bitmap* >'])
    register_ON_SimpleArray__ON_BrepTrimPoint_methods(root_module, root_module['ON_SimpleArray< ON_BrepTrimPoint >'])
    register_ON_SimpleArray__ON_BumpFunction_methods(root_module, root_module['ON_SimpleArray< ON_BumpFunction >'])
    register_ON_SimpleArray__ON_ClippingPlaneInfo_methods(root_module, root_module['ON_SimpleArray< ON_ClippingPlaneInfo >'])
    register_ON_SimpleArray__ON_Color_methods(root_module, root_module['ON_SimpleArray< ON_Color >'])
    register_ON_SimpleArray__ON_Curve__star___methods(root_module, root_module['ON_SimpleArray< ON_Curve* >'])
    register_ON_SimpleArray__ON_DisplayMaterialRef_methods(root_module, root_module['ON_SimpleArray< ON_DisplayMaterialRef >'])
    register_ON_SimpleArray__ON_HatchLoop__star___methods(root_module, root_module['ON_SimpleArray< ON_HatchLoop* >'])
    register_ON_SimpleArray__ON_HistoryRecord__star___methods(root_module, root_module['ON_SimpleArray< ON_HistoryRecord* >'])
    register_ON_SimpleArray__ON_Interval_methods(root_module, root_module['ON_SimpleArray< ON_Interval >'])
    register_ON_SimpleArray__ON_LinetypeSegment_methods(root_module, root_module['ON_SimpleArray< ON_LinetypeSegment >'])
    register_ON_SimpleArray__ON_MappingChannel_methods(root_module, root_module['ON_SimpleArray< ON_MappingChannel >'])
    register_ON_SimpleArray__ON_MeshFace_methods(root_module, root_module['ON_SimpleArray< ON_MeshFace >'])
    register_ON_SimpleArray__ON_MeshPart_methods(root_module, root_module['ON_SimpleArray< ON_MeshPart >'])
    register_ON_SimpleArray__ON_MeshTopologyEdge_methods(root_module, root_module['ON_SimpleArray< ON_MeshTopologyEdge >'])
    register_ON_SimpleArray__ON_MeshTopologyFace_methods(root_module, root_module['ON_SimpleArray< ON_MeshTopologyFace >'])
    register_ON_SimpleArray__ON_MeshTopologyVertex_methods(root_module, root_module['ON_SimpleArray< ON_MeshTopologyVertex >'])
    register_ON_SimpleArray__ON_ObjRef_IRefID_methods(root_module, root_module['ON_SimpleArray< ON_ObjRef_IRefID >'])
    register_ON_SimpleArray__ON_OffsetSurfaceValue_methods(root_module, root_module['ON_SimpleArray< ON_OffsetSurfaceValue >'])
    register_ON_SimpleArray__ON_Surface__star___methods(root_module, root_module['ON_SimpleArray< ON_Surface* >'])
    register_ON_SimpleArray__ON_SurfaceCurvature_methods(root_module, root_module['ON_SimpleArray< ON_SurfaceCurvature >'])
    register_ON_SimpleArray__ON_UUID_methods(root_module, root_module['ON_SimpleArray< ON_UUID >'])
    register_ON_SimpleArray__ON_UuidIndex_methods(root_module, root_module['ON_SimpleArray< ON_UuidIndex >'])
    register_ON_SimpleArray__ON_UuidPair_methods(root_module, root_module['ON_SimpleArray< ON_UuidPair >'])
    register_ON_SimpleArray__ON_Value__star___methods(root_module, root_module['ON_SimpleArray< ON_Value* >'])
    register_ON_SimpleArray__Bool_methods(root_module, root_module['ON_SimpleArray< bool >'])
    register_ON_SimpleArray__Double__star___methods(root_module, root_module['ON_SimpleArray< double* >'])
    register_ON_SimpleArray__Double_methods(root_module, root_module['ON_SimpleArray< double >'])
    register_ON_SimpleArray__Int_methods(root_module, root_module['ON_SimpleArray< int >'])
    register_ON_SimpleArray__TagON_2dex_methods(root_module, root_module['ON_SimpleArray< tagON_2dex >'])
    register_ON_SpaceMorph_methods(root_module, root_module['ON_SpaceMorph'])
    register_ON_Sphere_methods(root_module, root_module['ON_Sphere'])
    register_ON_String_methods(root_module, root_module['ON_String'])
    register_ON_Sum_methods(root_module, root_module['ON_Sum'])
    register_ON_SurfaceArray_methods(root_module, root_module['ON_SurfaceArray'])
    register_ON_SurfaceCurvature_methods(root_module, root_module['ON_SurfaceCurvature'])
    register_ON_SurfaceProperties_methods(root_module, root_module['ON_SurfaceProperties'])
    register_ON_TensorProduct_methods(root_module, root_module['ON_TensorProduct'])
    register_ON_TextLog_methods(root_module, root_module['ON_TextLog'])
    register_ON_Texture_methods(root_module, root_module['ON_Texture'])
    register_ON_TextureCoordinates_methods(root_module, root_module['ON_TextureCoordinates'])
    register_ON_TextureMapping_methods(root_module, root_module['ON_TextureMapping'])
    register_ON_Torus_methods(root_module, root_module['ON_Torus'])
    register_ON_U_methods(root_module, root_module['ON_U'])
    register_ON_UUID_methods(root_module, root_module['ON_UUID'])
    register_ON_UncompressStream_methods(root_module, root_module['ON_UncompressStream'])
    register_ON_UnicodeErrorParameters_methods(root_module, root_module['ON_UnicodeErrorParameters'])
    register_ON_UnitSystem_methods(root_module, root_module['ON_UnitSystem'])
    register_ON_UserData_methods(root_module, root_module['ON_UserData'])
    register_ON_UserDataHolder_methods(root_module, root_module['ON_UserDataHolder'])
    register_ON_UserString_methods(root_module, root_module['ON_UserString'])
    register_ON_UserStringList_methods(root_module, root_module['ON_UserStringList'])
    register_ON_UuidIndex_methods(root_module, root_module['ON_UuidIndex'])
    register_ON_UuidIndexList_methods(root_module, root_module['ON_UuidIndexList'])
    register_ON_UuidList_methods(root_module, root_module['ON_UuidList'])
    register_ON_UuidPair_methods(root_module, root_module['ON_UuidPair'])
    register_ON_UuidPairList_methods(root_module, root_module['ON_UuidPairList'])
    register_ON_WindowsBITMAPINFO_methods(root_module, root_module['ON_WindowsBITMAPINFO'])
    register_ON_WindowsBITMAPINFOHEADER_methods(root_module, root_module['ON_WindowsBITMAPINFOHEADER'])
    register_ON_WindowsRGBQUAD_methods(root_module, root_module['ON_WindowsRGBQUAD'])
    register_ON_Workspace_methods(root_module, root_module['ON_Workspace'])
    register_ON_Write3dmBufferArchive_methods(root_module, root_module['ON_Write3dmBufferArchive'])
    register_ON_X_EVENT_methods(root_module, root_module['ON_X_EVENT'])
    register_ON_Xform_methods(root_module, root_module['ON_Xform'])
    register_ON_wString_methods(root_module, root_module['ON_wString'])
    register_TagON_2dex_methods(root_module, root_module['tagON_2dex'])
    register_TagON_3dex_methods(root_module, root_module['tagON_3dex'])
    register_TagON_4dex_methods(root_module, root_module['tagON_4dex'])
    register_TagON_RECT_methods(root_module, root_module['tagON_RECT'])
    register_ON_2dPointArray_methods(root_module, root_module['ON_2dPointArray'])
    register_ON_2dVectorArray_methods(root_module, root_module['ON_2dVectorArray'])
    register_ON_2dexMap_methods(root_module, root_module['ON_2dexMap'])
    register_ON_2fPointArray_methods(root_module, root_module['ON_2fPointArray'])
    register_ON_2fVectorArray_methods(root_module, root_module['ON_2fVectorArray'])
    register_ON_3dPointArray_methods(root_module, root_module['ON_3dPointArray'])
    register_ON_3dVectorArray_methods(root_module, root_module['ON_3dVectorArray'])
    register_ON_3dmObjectAttributes_methods(root_module, root_module['ON_3dmObjectAttributes'])
    register_ON_3fPointArray_methods(root_module, root_module['ON_3fPointArray'])
    register_ON_3fVectorArray_methods(root_module, root_module['ON_3fVectorArray'])
    register_ON_4dPointArray_methods(root_module, root_module['ON_4dPointArray'])
    register_ON_4fPointArray_methods(root_module, root_module['ON_4fPointArray'])
    register_ON_Annotation2Text_methods(root_module, root_module['ON_Annotation2Text'])
    register_ON_Arc_methods(root_module, root_module['ON_Arc'])
    register_ON_BezierCageMorph_methods(root_module, root_module['ON_BezierCageMorph'])
    register_ON_Bitmap_methods(root_module, root_module['ON_Bitmap'])
    register_ON_BrepEdgeArray_methods(root_module, root_module['ON_BrepEdgeArray'])
    register_ON_BrepFaceArray_methods(root_module, root_module['ON_BrepFaceArray'])
    register_ON_BrepFaceSide_methods(root_module, root_module['ON_BrepFaceSide'])
    register_ON_BrepFaceSideArray_methods(root_module, root_module['ON_BrepFaceSideArray'])
    register_ON_BrepLoopArray_methods(root_module, root_module['ON_BrepLoopArray'])
    register_ON_BrepRegion_methods(root_module, root_module['ON_BrepRegion'])
    register_ON_BrepRegionArray_methods(root_module, root_module['ON_BrepRegionArray'])
    register_ON_BrepTrimArray_methods(root_module, root_module['ON_BrepTrimArray'])
    register_ON_BrepVertexArray_methods(root_module, root_module['ON_BrepVertexArray'])
    register_ON_CageMorph_methods(root_module, root_module['ON_CageMorph'])
    register_ON_CurveArray_methods(root_module, root_module['ON_CurveArray'])
    register_ON_DimStyle_methods(root_module, root_module['ON_DimStyle'])
    register_ON_DimensionExtra_methods(root_module, root_module['ON_DimensionExtra'])
    register_ON_DocumentUserStringList_methods(root_module, root_module['ON_DocumentUserStringList'])
    register_ON_EmbeddedBitmap_methods(root_module, root_module['ON_EmbeddedBitmap'])
    register_ON_EmbeddedFile_methods(root_module, root_module['ON_EmbeddedFile'])
    register_ON_Font_methods(root_module, root_module['ON_Font'])
    register_ON_Geometry_methods(root_module, root_module['ON_Geometry'])
    register_ON_Group_methods(root_module, root_module['ON_Group'])
    register_ON_Hatch_methods(root_module, root_module['ON_Hatch'])
    register_ON_HatchPattern_methods(root_module, root_module['ON_HatchPattern'])
    register_ON_HistoryRecord_methods(root_module, root_module['ON_HistoryRecord'])
    register_ON_InstanceDefinition_methods(root_module, root_module['ON_InstanceDefinition'])
    register_ON_InstanceRef_methods(root_module, root_module['ON_InstanceRef'])
    register_ON_Layer_methods(root_module, root_module['ON_Layer'])
    register_ON_Light_methods(root_module, root_module['ON_Light'])
    register_ON_Linetype_methods(root_module, root_module['ON_Linetype'])
    register_ON_Material_methods(root_module, root_module['ON_Material'])
    register_ON_Mesh_methods(root_module, root_module['ON_Mesh'])
    register_ON_MeshEdgeRef_methods(root_module, root_module['ON_MeshEdgeRef'])
    register_ON_MeshFaceRef_methods(root_module, root_module['ON_MeshFaceRef'])
    register_ON_MeshVertexRef_methods(root_module, root_module['ON_MeshVertexRef'])
    register_ON_MorphControl_methods(root_module, root_module['ON_MorphControl'])
    register_ON_NurbsCage_methods(root_module, root_module['ON_NurbsCage'])
    register_ON_ObjectRenderingAttributes_methods(root_module, root_module['ON_ObjectRenderingAttributes'])
    register_ON_Point_methods(root_module, root_module['ON_Point'])
    register_ON_PointCloud_methods(root_module, root_module['ON_PointCloud'])
    register_ON_PointGrid_methods(root_module, root_module['ON_PointGrid'])
    register_ON_Polyline_methods(root_module, root_module['ON_Polyline'])
    register_ON_Surface_methods(root_module, root_module['ON_Surface'])
    register_ON_SurfaceProxy_methods(root_module, root_module['ON_SurfaceProxy'])
    register_ON_TextDot_methods(root_module, root_module['ON_TextDot'])
    register_ON_TextExtra_methods(root_module, root_module['ON_TextExtra'])
    register_ON_UnknownUserData_methods(root_module, root_module['ON_UnknownUserData'])
    register_ON_Viewport_methods(root_module, root_module['ON_Viewport'])
    register_ON_WindowsBitmap_methods(root_module, root_module['ON_WindowsBitmap'])
    register_ON_WindowsBitmapEx_methods(root_module, root_module['ON_WindowsBitmapEx'])
    register_ON_Annotation_methods(root_module, root_module['ON_Annotation'])
    register_ON_Annotation2_methods(root_module, root_module['ON_Annotation2'])
    register_ON_AnnotationArrow_methods(root_module, root_module['ON_AnnotationArrow'])
    register_ON_AnnotationTextDot_methods(root_module, root_module['ON_AnnotationTextDot'])
    register_ON_Brep_methods(root_module, root_module['ON_Brep'])
    register_ON_BrepFace_methods(root_module, root_module['ON_BrepFace'])
    register_ON_BrepLoop_methods(root_module, root_module['ON_BrepLoop'])
    register_ON_BrepVertex_methods(root_module, root_module['ON_BrepVertex'])
    register_ON_Curve_methods(root_module, root_module['ON_Curve'])
    register_ON_CurveOnSurface_methods(root_module, root_module['ON_CurveOnSurface'])
    register_ON_CurveProxy_methods(root_module, root_module['ON_CurveProxy'])
    register_ON_DetailView_methods(root_module, root_module['ON_DetailView'])
    register_ON_Extrusion_methods(root_module, root_module['ON_Extrusion'])
    register_ON_Leader_methods(root_module, root_module['ON_Leader'])
    register_ON_Leader2_methods(root_module, root_module['ON_Leader2'])
    register_ON_LineCurve_methods(root_module, root_module['ON_LineCurve'])
    register_ON_LinearDimension_methods(root_module, root_module['ON_LinearDimension'])
    register_ON_LinearDimension2_methods(root_module, root_module['ON_LinearDimension2'])
    register_ON_NurbsCurve_methods(root_module, root_module['ON_NurbsCurve'])
    register_ON_NurbsSurface_methods(root_module, root_module['ON_NurbsSurface'])
    register_ON_OffsetSurface_methods(root_module, root_module['ON_OffsetSurface'])
    register_ON_OrdinateDimension2_methods(root_module, root_module['ON_OrdinateDimension2'])
    register_ON_PlaneSurface_methods(root_module, root_module['ON_PlaneSurface'])
    register_ON_PolyCurve_methods(root_module, root_module['ON_PolyCurve'])
    register_ON_PolylineCurve_methods(root_module, root_module['ON_PolylineCurve'])
    register_ON_RadialDimension_methods(root_module, root_module['ON_RadialDimension'])
    register_ON_RadialDimension2_methods(root_module, root_module['ON_RadialDimension2'])
    register_ON_RevSurface_methods(root_module, root_module['ON_RevSurface'])
    register_ON_SumSurface_methods(root_module, root_module['ON_SumSurface'])
    register_ON_TextEntity_methods(root_module, root_module['ON_TextEntity'])
    register_ON_TextEntity2_methods(root_module, root_module['ON_TextEntity2'])
    register_ON_AngularDimension_methods(root_module, root_module['ON_AngularDimension'])
    register_ON_AngularDimension2_methods(root_module, root_module['ON_AngularDimension2'])
    register_ON_ArcCurve_methods(root_module, root_module['ON_ArcCurve'])
    register_ON_BrepEdge_methods(root_module, root_module['ON_BrepEdge'])
    register_ON_BrepTrim_methods(root_module, root_module['ON_BrepTrim'])
    register_ON_ClippingPlaneSurface_methods(root_module, root_module['ON_ClippingPlaneSurface'])
    return

def register_ON_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON const &', 'arg0')])
    cls.add_method('ActiveSpace', 
                   'ON::active_space', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('AnnotationType', 
                   'ON::eAnnotationType', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('ArchiveMode', 
                   'ON::archive_mode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('Begin', 
                   'void', 
                   [], 
                   is_static=True)
    cls.add_method('BitmapType', 
                   'ON::bitmap_type', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('CloseAllFiles', 
                   'int', 
                   [], 
                   is_static=True)
    cls.add_method('CloseFile', 
                   'int', 
                   [param('FILE *', 'arg0')], 
                   is_static=True)
    cls.add_method('Continuity', 
                   'ON::continuity', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('CoordinateSystem', 
                   'ON::coordinate_system', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('CubicLoftEndCondition', 
                   'ON::cubic_loft_end_condition', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('CurvatureStyle', 
                   'ON::curvature_style', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('CurveStyle', 
                   'ON::curve_style', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('DisplayMode', 
                   'ON::display_mode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('DistanceDisplayMode', 
                   'ON::distance_display_mode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('DocumentationBranch', 
                   'char const *', 
                   [], 
                   is_static=True)
    cls.add_method('DocumentationRevision', 
                   'char const *', 
                   [], 
                   is_static=True)
    cls.add_method('End', 
                   'void', 
                   [], 
                   is_static=True)
    cls.add_method('Endian', 
                   'ON::endian', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('Endian', 
                   'ON::endian', 
                   [], 
                   is_static=True)
    cls.add_method('ExceptionType', 
                   'ON::exception_type', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('GetFileStats', 
                   'bool', 
                   [param('wchar_t const *', 'filename'), param('size_t *', 'filesize'), param('time_t *', 'create_time'), param('time_t *', 'lastmodify_time')], 
                   is_static=True)
    cls.add_method('GetFileStats', 
                   'bool', 
                   [param('FILE *', 'fp'), param('size_t *', 'filesize'), param('time_t *', 'create_time'), param('time_t *', 'lastmodify_time')], 
                   is_static=True)
    cls.add_method('IsDirectory', 
                   'bool', 
                   [param('wchar_t const *', 'pathname')], 
                   is_static=True)
    cls.add_method('IsDirectory', 
                   'bool', 
                   [param('char const *', 'utf8pathname')], 
                   is_static=True)
    cls.add_method('IsNameReferenceDelimiter', 
                   'wchar_t const *', 
                   [param('wchar_t const *', 's')], 
                   is_static=True)
    cls.add_method('IsOpenNURBSFile', 
                   'int', 
                   [param('wchar_t const *', 'pathname')], 
                   is_static=True)
    cls.add_method('IsOpenNURBSFile', 
                   'int', 
                   [param('char const *', 'utf8pathname')], 
                   is_static=True)
    cls.add_method('IsOpenNURBSFile', 
                   'int', 
                   [param('FILE *', 'fp')], 
                   is_static=True)
    cls.add_method('IsParallelProjection', 
                   'bool', 
                   [param('ON::view_projection', 'projection')], 
                   is_static=True)
    cls.add_method('IsPerspectiveProjection', 
                   'bool', 
                   [param('ON::view_projection', 'projection')], 
                   is_static=True)
    cls.add_method('KnotStyle', 
                   'ON::knot_style', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('LayerMode', 
                   'ON::layer_mode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('LightStyle', 
                   'ON::light_style', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('MeshType', 
                   'ON::mesh_type', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('NameReferenceDelimiter', 
                   'wchar_t const *', 
                   [], 
                   is_static=True)
    cls.add_method('NameReferenceDelimiterLength', 
                   'unsigned int', 
                   [], 
                   is_static=True)
    cls.add_method('OSnapMode', 
                   'ON::osnap_mode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('ObjectColorSource', 
                   'ON::object_color_source', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('ObjectDecoration', 
                   'ON::object_decoration', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('ObjectLinetypeSource', 
                   'ON::object_linetype_source', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('ObjectMaterialSource', 
                   'ON::object_material_source', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('ObjectMode', 
                   'ON::object_mode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('ObjectType', 
                   'ON::object_type', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('OpenFile', 
                   'FILE *', 
                   [param('char const *', 'filename'), param('char const *', 'filemode')], 
                   is_static=True)
    cls.add_method('OpenFile', 
                   'FILE *', 
                   [param('wchar_t const *', 'filename'), param('wchar_t const *', 'filemode')], 
                   is_static=True)
    cls.add_method('ParametricContinuity', 
                   'ON::continuity', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('PlotColorSource', 
                   'ON::plot_color_source', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('PlotWeightSource', 
                   'ON::plot_weight_source', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('PointStyle', 
                   'ON::point_style', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('PolylineContinuity', 
                   'ON::continuity', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('SortAlgorithm', 
                   'ON::sort_algorithm', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('SourceBranch', 
                   'char const *', 
                   [], 
                   is_static=True)
    cls.add_method('SourceRevision', 
                   'char const *', 
                   [], 
                   is_static=True)
    cls.add_method('SurfaceStyle', 
                   'ON::surface_style', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('TextDisplayMode', 
                   'ON::eTextDisplayMode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('TextureMode', 
                   'ON::texture_mode', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('UnitScale', 
                   'double', 
                   [param('ON::unit_system', 'us_from'), param('ON::unit_system', 'us_to')], 
                   is_static=True)
    cls.add_method('UnitScale', 
                   'double', 
                   [param('ON_UnitSystem const &', 'us_from'), param('ON_UnitSystem const &', 'us_to')], 
                   is_static=True)
    cls.add_method('UnitScale', 
                   'double', 
                   [param('ON::unit_system', 'us_from'), param('ON_UnitSystem const &', 'us_to')], 
                   is_static=True)
    cls.add_method('UnitScale', 
                   'double', 
                   [param('ON_UnitSystem const &', 'us_from'), param('ON::unit_system', 'us_to')], 
                   is_static=True)
    cls.add_method('UnitScale', 
                   'double', 
                   [param('ON_3dmUnitsAndTolerances const &', 'us_from'), param('ON_3dmUnitsAndTolerances const &', 'us_to')], 
                   is_static=True)
    cls.add_method('UnitSystem', 
                   'ON::unit_system', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('Version', 
                   'int', 
                   [], 
                   is_static=True)
    cls.add_method('ViewProjection', 
                   'ON::view_projection', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('ViewType', 
                   'ON::view_type', 
                   [param('int', 'arg0')], 
                   is_static=True)
    return

def register_ONX_Model_methods(root_module, cls):
    cls.add_instance_attribute('m_3dm_file_version', 'int', is_const=False)
    cls.add_instance_attribute('m_3dm_opennurbs_version', 'int', is_const=False)
    cls.add_instance_attribute('m_sStartSectionComments', 'ON_String', is_const=False)
    cls.add_instance_attribute('m_properties', 'ON_3dmProperties', is_const=False)
    cls.add_instance_attribute('m_settings', 'ON_3dmSettings', is_const=False)
    cls.add_instance_attribute('m_bitmap_table', 'ON_SimpleArray< ON_Bitmap * >', is_const=False)
    cls.add_instance_attribute('m_mapping_table', 'ON_ObjectArray< ON_TextureMapping >', is_const=False)
    cls.add_instance_attribute('m_material_table', 'ON_ObjectArray< ON_Material >', is_const=False)
    cls.add_instance_attribute('m_linetype_table', 'ON_ObjectArray< ON_Linetype >', is_const=False)
    cls.add_instance_attribute('m_layer_table', 'ON_ObjectArray< ON_Layer >', is_const=False)
    cls.add_instance_attribute('m_group_table', 'ON_ObjectArray< ON_Group >', is_const=False)
    cls.add_instance_attribute('m_font_table', 'ON_ObjectArray< ON_Font >', is_const=False)
    cls.add_instance_attribute('m_dimstyle_table', 'ON_ObjectArray< ON_DimStyle >', is_const=False)
    cls.add_instance_attribute('m_light_table', 'ON_ClassArray< ONX_Model_RenderLight >', is_const=False)
    cls.add_instance_attribute('m_hatch_pattern_table', 'ON_ObjectArray< ON_HatchPattern >', is_const=False)
    cls.add_instance_attribute('m_idef_table', 'ON_ObjectArray< ON_InstanceDefinition >', is_const=False)
    cls.add_instance_attribute('m_object_table', 'ON_ClassArray< ONX_Model_Object >', is_const=False)
    cls.add_instance_attribute('m_history_record_table', 'ON_SimpleArray< ON_HistoryRecord * >', is_const=False)
    cls.add_instance_attribute('m_userdata_table', 'ON_ClassArray< ONX_Model_UserData >', is_const=False)
    cls.add_instance_attribute('m_mapping_id_index', 'ON_UuidIndexList', is_const=False)
    cls.add_instance_attribute('m_material_id_index', 'ON_UuidIndexList', is_const=False)
    cls.add_instance_attribute('m_object_id_index', 'ON_UuidIndexList', is_const=False)
    cls.add_instance_attribute('m_idef_id_index', 'ON_UuidIndexList', is_const=False)
    cls.add_instance_attribute('m_file_length', 'size_t', is_const=False)
    cls.add_instance_attribute('m_crc_error_count', 'int', is_const=False)
    cls.add_constructor([])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive'), param('ON_TextLog *', 'error_log', default_value='0')])
    cls.add_method('Read', 
                   'bool', 
                   [param('char const *', 'filename'), param('ON_TextLog *', 'error_log', default_value='0')])
    cls.add_method('Read', 
                   'bool', 
                   [param('wchar_t const *', 'filename'), param('ON_TextLog *', 'error_log', default_value='0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive'), param('int', 'version', default_value='0'), param('char const *', 'sStartSectionComment', default_value='0'), param('ON_TextLog *', 'error_log', default_value='0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('char const *', 'filename'), param('int', 'version', default_value='0'), param('char const *', 'sStartSectionComment', default_value='0'), param('ON_TextLog *', 'error_log', default_value='0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('wchar_t const *', 'filename'), param('int', 'version', default_value='0'), param('char const *', 'sStartSectionComment', default_value='0'), param('ON_TextLog *', 'error_log', default_value='0')])
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True)
    cls.add_method('Polish', 
                   'void', 
                   [], 
                   is_virtual=True)
    cls.add_method('Audit', 
                   'int', 
                   [param('bool', 'bAttemptRepair'), param('int *', 'repair_count'), param('ON_TextLog *', 'text_log'), param('ON_SimpleArray< int > *', 'warnings')], 
                   is_virtual=True)
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('GetRenderMaterial', 
                   'void', 
                   [param('ON_3dmObjectAttributes const &', 'attributes'), param('ON_Material &', 'material')], 
                   is_const=True)
    cls.add_method('GetRenderMaterial', 
                   'void', 
                   [param('int', 'object_index'), param('ON_Material &', 'material')], 
                   is_const=True)
    cls.add_method('GetLinetype', 
                   'void', 
                   [param('ON_3dmObjectAttributes const &', 'attributes'), param('ON_Linetype &', 'linetype')], 
                   is_const=True)
    cls.add_method('GetLinetype', 
                   'void', 
                   [param('int', 'object_index'), param('ON_Linetype &', 'linetype')], 
                   is_const=True)
    cls.add_method('WireframeColor', 
                   'ON_Color', 
                   [param('ON_3dmObjectAttributes const &', 'attributes')], 
                   is_const=True)
    cls.add_method('WireframeColor', 
                   'ON_Color', 
                   [param('int', 'object_index')], 
                   is_const=True)
    cls.add_method('ObjectIndex', 
                   'int', 
                   [param('ON_UUID', 'object_uuid')], 
                   is_const=True, is_virtual=True)
    cls.add_method('IDefIndex', 
                   'int', 
                   [param('ON_UUID', 'idef_uuid')], 
                   is_const=True, is_virtual=True)
    cls.add_method('IDefIndex', 
                   'int', 
                   [param('wchar_t const *', 'idef_name')], 
                   is_const=True, is_virtual=True)
    cls.add_method('GetUnusedIDefName', 
                   'void', 
                   [param('ON_wString &', 'idef_name')], 
                   is_const=True, is_virtual=True)
    cls.add_method('UsesIDef', 
                   'int', 
                   [param('ON_InstanceRef const &', 'iref'), param('ON_UUID', 'idef_uuid')], 
                   is_const=True, is_virtual=True)
    cls.add_method('LayerIndex', 
                   'int', 
                   [param('wchar_t const *', 'layer_name')], 
                   is_const=True, is_virtual=True)
    cls.add_method('GetUnusedLayerName', 
                   'void', 
                   [param('ON_wString &', 'layer_name')], 
                   is_const=True, is_virtual=True)
    cls.add_method('SetDocumentUserString', 
                   'bool', 
                   [param('wchar_t const *', 'key'), param('wchar_t const *', 'string_value')])
    cls.add_method('GetDocumentUserString', 
                   'bool', 
                   [param('wchar_t const *', 'key'), param('ON_wString &', 'string_value')], 
                   is_const=True)
    cls.add_method('GetDocumentUserStrings', 
                   'int', 
                   [param('ON_ClassArray< ON_UserString > &', 'user_strings')], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpSummary', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpBitmapTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpTextureMappingTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpMaterialTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpLinetypeTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpLayerTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpLightTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpGroupTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpFontTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpDimStyleTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpHatchPatternTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpIDefTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpObjectTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpHistoryRecordTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DumpUserDataTable', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('DestroyCache', 
                   'void', 
                   [])
    cls.add_method('IsRDKDocumentInformation', 
                   'bool', 
                   [param('ONX_Model_UserData const &', 'docud')], 
                   is_static=True)
    cls.add_method('GetRDKDocumentInformation', 
                   'bool', 
                   [param('ONX_Model_UserData const &', 'docud'), param('ON_wString &', 'rdk_xml_document_data')], 
                   is_static=True)
    cls.add_method('IsRDKObjectInformation', 
                   'bool', 
                   [param('ON_UserData const &', 'objectud')], 
                   is_static=True)
    cls.add_method('GetRDKObjectInformation', 
                   'bool', 
                   [param('ON_Object const &', 'object'), param('ON_wString &', 'rdk_xml_object_data')], 
                   is_static=True)
    return

def register_ONX_Model_Object_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ONX_Model_Object const &', 'arg0')])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_attributes', 'ON_3dmObjectAttributes', is_const=False)
    cls.add_instance_attribute('m_bDeleteObject', 'bool', is_const=False)
    cls.add_instance_attribute('m_object', 'ON_Object const *', is_const=False)
    return

def register_ONX_Model_RenderLight_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ONX_Model_RenderLight const &', 'arg0')])
    cls.add_instance_attribute('m_attributes', 'ON_3dmObjectAttributes', is_const=False)
    cls.add_instance_attribute('m_light', 'ON_Light', is_const=False)
    return

def register_ONX_Model_UserData_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ONX_Model_UserData const &', 'arg0')])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_goo', 'ON_3dmGoo', is_const=False)
    cls.add_instance_attribute('m_usertable_3dm_version', 'int', is_const=False)
    cls.add_instance_attribute('m_usertable_opennurbs_version', 'int', is_const=False)
    cls.add_instance_attribute('m_uuid', 'ON_UUID', is_const=False)
    return

def register_ON_2dPoint_methods(root_module, cls):
    cls.add_inplace_numeric_operator('*=', param('double', u'right'))
    cls.add_inplace_numeric_operator('/=', param('double', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_2dPoint const &', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_2dVector const &', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_3dVector const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_2dPoint const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_2dVector const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('int', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('int', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('float', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('float', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('double', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('double', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dVector'], root_module['ON_2dPoint'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_2dPoint'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_2dPoint'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_2dPoint'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_2dPoint'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dVector'], root_module['ON_2dPoint'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_2dPoint'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_2dPoint'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_2dPoint'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_2dPoint'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dPoint'], root_module['ON_2dPoint'], param('ON_Xform const &', u'right'))
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_constructor([param('ON_2dPoint const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 'x'), param('double', 'y')])
    cls.add_constructor([param('ON_3dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_4dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_2dVector const &', 'arg0')])
    cls.add_constructor([param('ON_3dVector const &', 'arg0')])
    cls.add_constructor([param('double const *', 'arg0')])
    cls.add_constructor([param('ON_2fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_4fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_2fVector const &', 'arg0')])
    cls.add_constructor([param('ON_3fVector const &', 'arg0')])
    cls.add_constructor([param('float const *', 'arg0')])
    cls.add_method('DistanceTo', 
                   'double', 
                   [param('ON_2dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsUnsetPoint', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'angle'), param('ON_2dPoint const &', 'center')])
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_2dPoint const &', 'center')])
    cls.add_method('Set', 
                   'void', 
                   [param('double', 'x'), param('double', 'y')])
    cls.add_method('Transform', 
                   'void', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_static_attribute('Origin', 'ON_2dPoint const', is_const=True)
    cls.add_static_attribute('UnsetPoint', 'ON_2dPoint const', is_const=True)
    cls.add_instance_attribute('x', 'double', is_const=False)
    cls.add_instance_attribute('y', 'double', is_const=False)
    return

def register_ON_2dVector_methods(root_module, cls):
    cls.add_unary_numeric_operator('-')
    cls.add_inplace_numeric_operator('*=', param('double', u'right'))
    cls.add_inplace_numeric_operator('/=', param('double', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_2dVector const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dVector'], root_module['ON_2dVector'], param('int', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_2dVector'], root_module['ON_2dVector'], param('int', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dVector'], root_module['ON_2dVector'], param('float', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_2dVector'], root_module['ON_2dVector'], param('float', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dVector'], root_module['ON_2dVector'], param('double', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_2dVector'], root_module['ON_2dVector'], param('double', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dVector'], root_module['ON_2dVector'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dPoint'], root_module['ON_2dVector'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dVector'], root_module['ON_2dVector'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dPoint'], root_module['ON_2dVector'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dVector'], root_module['ON_2dVector'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_2dVector'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_2dVector'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_2dVector'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dVector'], root_module['ON_2dVector'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_2dPoint'], root_module['ON_2dVector'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dVector'], root_module['ON_2dVector'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_2dPoint'], root_module['ON_2dVector'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dVector'], root_module['ON_2dVector'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_2dVector'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_2dVector'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_2dVector'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_2dVector'], root_module['ON_2dVector'], param('ON_Xform const &', u'right'))
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_constructor([param('ON_2dVector const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 'x'), param('double', 'y')])
    cls.add_constructor([param('ON_3dVector const &', 'arg0')])
    cls.add_constructor([param('ON_2dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3dPoint const &', 'arg0')])
    cls.add_constructor([param('double const *', 'arg0')])
    cls.add_constructor([param('ON_2fVector const &', 'arg0')])
    cls.add_constructor([param('ON_3fVector const &', 'arg0')])
    cls.add_constructor([param('ON_2fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3fPoint const &', 'arg0')])
    cls.add_constructor([param('float const *', 'arg0')])
    cls.add_method('Decompose', 
                   'bool', 
                   [param('ON_2dVector const &', 'arg0'), param('ON_2dVector const &', 'arg1'), param('double *', 'arg2'), param('double *', 'arg3')], 
                   is_const=True)
    cls.add_method('IsParallelTo', 
                   'int', 
                   [param('ON_2dVector const &', 'other'), param('double', 'angle_tolerance', default_value='1.74532925199432954743716805978692718781530857086e-2')], 
                   is_const=True)
    cls.add_method('IsPerpendicularTo', 
                   'bool', 
                   [param('ON_2dVector const &', 'other'), param('double', 'angle_tolerance', default_value='1.74532925199432954743716805978692718781530857086e-2')], 
                   is_const=True)
    cls.add_method('IsTiny', 
                   'bool', 
                   [param('double', 'tiny_tol', default_value='2.3283064365386962890625e-10')], 
                   is_const=True)
    cls.add_method('IsUnitVector', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsUnsetVector', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsZero', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Length', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('LengthSquared', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('PerpendicularTo', 
                   'bool', 
                   [param('ON_2dVector const &', 'arg0')])
    cls.add_method('PerpendicularTo', 
                   'bool', 
                   [param('ON_2dPoint const &', 'arg0'), param('ON_2dPoint const &', 'arg1')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'angle')])
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle')])
    cls.add_method('Set', 
                   'void', 
                   [param('double', 'x'), param('double', 'y')])
    cls.add_method('Transform', 
                   'void', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('UnitVector', 
                   'ON_2dVector const &', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('Unitize', 
                   'bool', 
                   [])
    cls.add_method('WedgeProduct', 
                   'double', 
                   [param('ON_2dVector const &', 'B')], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_static_attribute('UnsetVector', 'ON_2dVector const', is_const=True)
    cls.add_static_attribute('XAxis', 'ON_2dVector const', is_const=True)
    cls.add_static_attribute('YAxis', 'ON_2dVector const', is_const=True)
    cls.add_static_attribute('ZeroVector', 'ON_2dVector const', is_const=True)
    cls.add_instance_attribute('x', 'double', is_const=False)
    cls.add_instance_attribute('y', 'double', is_const=False)
    return

def register_ON_3DM_BIG_CHUNK_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3DM_BIG_CHUNK const &', 'arg0')])
    cls.add_method('Length', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_instance_attribute('m_bLongChunk', 'ON__UINT8', is_const=False)
    cls.add_instance_attribute('m_big_offset', 'ON__UINT64', is_const=False)
    cls.add_instance_attribute('m_big_value', 'ON__INT64', is_const=False)
    cls.add_instance_attribute('m_crc16', 'ON__UINT16', is_const=False)
    cls.add_instance_attribute('m_crc32', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('m_do_crc16', 'ON__UINT8', is_const=False)
    cls.add_instance_attribute('m_do_crc32', 'ON__UINT8', is_const=False)
    cls.add_instance_attribute('m_reserved1', 'ON__UINT8', is_const=False)
    cls.add_instance_attribute('m_reserved2', 'ON__UINT8', is_const=False)
    cls.add_instance_attribute('m_reserved3', 'ON__UINT8', is_const=False)
    cls.add_instance_attribute('m_typecode', 'ON__UINT32', is_const=False)
    return

def register_ON_3DM_CHUNK_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3DM_CHUNK const &', 'arg0')])
    cls.add_instance_attribute('m_crc16', 'ON__UINT16', is_const=False)
    cls.add_instance_attribute('m_crc32', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('m_do_crc16', 'ON__UINT16', is_const=False)
    cls.add_instance_attribute('m_do_crc32', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('m_do_length', 'int', is_const=False)
    cls.add_instance_attribute('m_offset', 'size_t', is_const=False)
    cls.add_instance_attribute('m_typecode', 'unsigned int', is_const=False)
    cls.add_instance_attribute('m_value', 'int', is_const=False)
    return

def register_ON_3dPoint_methods(root_module, cls):
    cls.add_inplace_numeric_operator('*=', param('double', u'right'))
    cls.add_inplace_numeric_operator('/=', param('double', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_3dPoint const &', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_3dVector const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_3dPoint const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('int', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('int', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('float', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('float', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('double', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('double', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dPoint'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dPoint'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dPoint'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dPoint'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dPoint'], root_module['ON_3dPoint'], param('ON_Xform const &', u'right'))
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_constructor([param('ON_3dPoint const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 'x'), param('double', 'y'), param('double', 'z')])
    cls.add_constructor([param('ON_2dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_4dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_2dVector const &', 'arg0')])
    cls.add_constructor([param('ON_3dVector const &', 'arg0')])
    cls.add_constructor([param('double const *', 'arg0')])
    cls.add_constructor([param('ON_2fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_4fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_2fVector const &', 'arg0')])
    cls.add_constructor([param('ON_3fVector const &', 'arg0')])
    cls.add_constructor([param('float const *', 'arg0')])
    cls.add_method('DistanceTo', 
                   'double', 
                   [param('ON_3dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Fuzz', 
                   'double', 
                   [param('double', 'tolerance', default_value='2.3283064365386962890625e-10')], 
                   is_const=True)
    cls.add_method('IsUnsetPoint', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'angle'), param('ON_3dVector const &', 'axis'), param('ON_3dPoint const &', 'center')])
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis'), param('ON_3dPoint const &', 'center')])
    cls.add_method('Set', 
                   'void', 
                   [param('double', 'x'), param('double', 'y'), param('double', 'z')])
    cls.add_method('Transform', 
                   'void', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_static_attribute('Origin', 'ON_3dPoint const', is_const=True)
    cls.add_static_attribute('UnsetPoint', 'ON_3dPoint const', is_const=True)
    cls.add_instance_attribute('x', 'double', is_const=False)
    cls.add_instance_attribute('y', 'double', is_const=False)
    cls.add_instance_attribute('z', 'double', is_const=False)
    return

def register_ON_3dRay_methods(root_module, cls):
    cls.add_constructor([param('ON_3dRay const &', 'arg0')])
    cls.add_constructor([])
    cls.add_instance_attribute('m_P', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_V', 'ON_3dVector', is_const=False)
    return

def register_ON_3dVector_methods(root_module, cls):
    cls.add_unary_numeric_operator('-')
    cls.add_inplace_numeric_operator('*=', param('double', u'right'))
    cls.add_inplace_numeric_operator('/=', param('double', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_3dVector const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dVector'], root_module['ON_3dVector'], param('int', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_3dVector'], root_module['ON_3dVector'], param('int', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dVector'], root_module['ON_3dVector'], param('float', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_3dVector'], root_module['ON_3dVector'], param('float', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dVector'], root_module['ON_3dVector'], param('double', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_3dVector'], root_module['ON_3dVector'], param('double', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_3dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_3dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_2dVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_2dPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_3fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_3fPoint const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_2fVector const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_3dPoint'], root_module['ON_3dVector'], param('ON_2fPoint const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_3dVector'], root_module['ON_3dVector'], param('ON_Xform const &', u'right'))
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_constructor([param('ON_3dVector const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 'x'), param('double', 'y'), param('double', 'z')])
    cls.add_constructor([param('ON_2dVector const &', 'arg0')])
    cls.add_constructor([param('ON_2dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3dPoint const &', 'arg0')])
    cls.add_constructor([param('double const *', 'arg0')])
    cls.add_constructor([param('ON_2fVector const &', 'arg0')])
    cls.add_constructor([param('ON_3fVector const &', 'arg0')])
    cls.add_constructor([param('ON_2fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3fPoint const &', 'arg0')])
    cls.add_constructor([param('float const *', 'arg0')])
    cls.add_method('Decompose', 
                   'bool', 
                   [param('ON_3dVector const &', 'arg0'), param('ON_3dVector const &', 'arg1'), param('ON_3dVector const &', 'arg2'), param('double *', 'arg3'), param('double *', 'arg4'), param('double *', 'arg5')], 
                   is_const=True)
    cls.add_method('Fuzz', 
                   'double', 
                   [param('double', 'tolerance', default_value='2.3283064365386962890625e-10')], 
                   is_const=True)
    cls.add_method('IsParallelTo', 
                   'int', 
                   [param('ON_3dVector const &', 'other'), param('double', 'angle_tolerance', default_value='1.74532925199432954743716805978692718781530857086e-2')], 
                   is_const=True)
    cls.add_method('IsPerpendicularTo', 
                   'bool', 
                   [param('ON_3dVector const &', 'other'), param('double', 'angle_tolerance', default_value='1.74532925199432954743716805978692718781530857086e-2')], 
                   is_const=True)
    cls.add_method('IsTiny', 
                   'bool', 
                   [param('double', 'tiny_tol', default_value='2.3283064365386962890625e-10')], 
                   is_const=True)
    cls.add_method('IsUnitVector', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsUnsetVector', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsZero', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Length', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('LengthAndUnitize', 
                   'double', 
                   [])
    cls.add_method('LengthSquared', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('PerpendicularTo', 
                   'bool', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_method('PerpendicularTo', 
                   'bool', 
                   [param('ON_3dPoint const &', 'arg0'), param('ON_3dPoint const &', 'arg1'), param('ON_3dPoint const &', 'arg2')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'angle'), param('ON_3dVector const &', 'axis')])
    cls.add_method('Rotate', 
                   'void', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis')])
    cls.add_method('Set', 
                   'void', 
                   [param('double', 'x'), param('double', 'y'), param('double', 'z')])
    cls.add_method('Transform', 
                   'void', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('UnitVector', 
                   'ON_3dVector const &', 
                   [param('int', 'arg0')], 
                   is_static=True)
    cls.add_method('Unitize', 
                   'bool', 
                   [])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_static_attribute('UnsetVector', 'ON_3dVector const', is_const=True)
    cls.add_static_attribute('XAxis', 'ON_3dVector const', is_const=True)
    cls.add_static_attribute('YAxis', 'ON_3dVector const', is_const=True)
    cls.add_static_attribute('ZAxis', 'ON_3dVector const', is_const=True)
    cls.add_static_attribute('ZeroVector', 'ON_3dVector const', is_const=True)
    cls.add_instance_attribute('x', 'double', is_const=False)
    cls.add_instance_attribute('y', 'double', is_const=False)
    cls.add_instance_attribute('z', 'double', is_const=False)
    return

def register_ON_3dmAnnotationSettings_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmAnnotationSettings const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('EnableAnnotationScaling', 
                   'void', 
                   [param('bool', 'bEnable')])
    cls.add_method('EnableHatchScaling', 
                   'void', 
                   [param('bool', 'bEnable')])
    cls.add_method('IsAnnotationScalingEnabled', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsHatchScalingEnabled', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('SetWorldViewHatchScale', 
                   'void', 
                   [param('double', 'world_view_hatch_scale')])
    cls.add_method('SetWorldViewTextScale', 
                   'void', 
                   [param('double', 'world_view_text_scale')])
    cls.add_method('WorldViewHatchScale', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('WorldViewTextScale', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_angleformat', 'int', is_const=False)
    cls.add_instance_attribute('m_angularunits', 'int', is_const=False)
    cls.add_instance_attribute('m_arrowlength', 'double', is_const=False)
    cls.add_instance_attribute('m_arrowtype', 'int', is_const=False)
    cls.add_instance_attribute('m_arrowwidth', 'double', is_const=False)
    cls.add_instance_attribute('m_centermark', 'double', is_const=False)
    cls.add_instance_attribute('m_dimexe', 'double', is_const=False)
    cls.add_instance_attribute('m_dimexo', 'double', is_const=False)
    cls.add_instance_attribute('m_dimscale', 'double', is_const=False)
    cls.add_instance_attribute('m_dimunits', 'ON::unit_system', is_const=False)
    cls.add_instance_attribute('m_facename', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_lengthformat', 'int', is_const=False)
    cls.add_instance_attribute('m_resolution', 'int', is_const=False)
    cls.add_instance_attribute('m_textalign', 'int', is_const=False)
    cls.add_instance_attribute('m_textheight', 'double', is_const=False)
    return

def register_ON_3dmApplication_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmApplication const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_application_URL', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_application_details', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_application_name', 'ON_wString', is_const=False)
    return

def register_ON_3dmConstructionPlane_methods(root_module, cls):
    cls.add_constructor([param('ON_3dmConstructionPlane const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bDepthBuffer', 'bool', is_const=False)
    cls.add_instance_attribute('m_grid_line_count', 'int', is_const=False)
    cls.add_instance_attribute('m_grid_spacing', 'double', is_const=False)
    cls.add_instance_attribute('m_grid_thick_frequency', 'int', is_const=False)
    cls.add_instance_attribute('m_name', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_plane', 'ON_Plane', is_const=False)
    cls.add_instance_attribute('m_snap_spacing', 'double', is_const=False)
    return

def register_ON_3dmConstructionPlaneGridDefaults_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmConstructionPlaneGridDefaults const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bShowGrid', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bShowGridAxes', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bShowWorldAxes', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_grid_line_count', 'int', is_const=False)
    cls.add_instance_attribute('m_grid_spacing', 'double', is_const=False)
    cls.add_instance_attribute('m_grid_thick_frequency', 'int', is_const=False)
    cls.add_instance_attribute('m_snap_spacing', 'double', is_const=False)
    return

def register_ON_3dmGoo_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmGoo const &', 'arg0')])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_goo', 'unsigned char *', is_const=False)
    cls.add_instance_attribute('m_next_goo', 'ON_3dmGoo *', is_const=False)
    cls.add_instance_attribute('m_prev_goo', 'ON_3dmGoo *', is_const=False)
    cls.add_instance_attribute('m_typecode', 'unsigned int', is_const=False)
    cls.add_instance_attribute('m_value', 'int', is_const=False)
    return

def register_ON_3dmIOSettings_methods(root_module, cls):
    cls.add_constructor([param('ON_3dmIOSettings const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bSaveTextureBitmapsInFile', 'bool', is_const=False)
    cls.add_instance_attribute('m_idef_link_update', 'int', is_const=False)
    return

def register_ON_3dmNotes_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmNotes const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bHTML', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bVisible', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_notes', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_window_bottom', 'int', is_const=False)
    cls.add_instance_attribute('m_window_left', 'int', is_const=False)
    cls.add_instance_attribute('m_window_right', 'int', is_const=False)
    cls.add_instance_attribute('m_window_top', 'int', is_const=False)
    return

def register_ON_3dmPageSettings_methods(root_module, cls):
    cls.add_constructor([param('ON_3dmPageSettings const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')], 
                   is_const=True)
    cls.add_instance_attribute('m_bottom_margin_mm', 'double', is_const=False)
    cls.add_instance_attribute('m_height_mm', 'double', is_const=False)
    cls.add_instance_attribute('m_left_margin_mm', 'double', is_const=False)
    cls.add_instance_attribute('m_page_number', 'int', is_const=False)
    cls.add_instance_attribute('m_printer_name', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_right_margin_mm', 'double', is_const=False)
    cls.add_instance_attribute('m_top_margin_mm', 'double', is_const=False)
    cls.add_instance_attribute('m_width_mm', 'double', is_const=False)
    return

def register_ON_3dmProperties_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmProperties const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_Application', 'ON_3dmApplication', is_const=False)
    cls.add_instance_attribute('m_Notes', 'ON_3dmNotes', is_const=False)
    cls.add_instance_attribute('m_PreviewImage', 'ON_WindowsBitmap', is_const=False)
    cls.add_instance_attribute('m_RevisionHistory', 'ON_3dmRevisionHistory', is_const=False)
    return

def register_ON_3dmRenderSettings_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmRenderSettings const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('ScaleBackgroundToFit', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('SetScaleBackgroundToFit', 
                   'void', 
                   [param('bool', 'bScaleBackgroundToFit')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_ambient_light', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_antialias_style', 'int', is_const=False)
    cls.add_instance_attribute('m_bCustomImageSize', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bDepthCue', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bFlatShade', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bRenderAnnotation', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bRenderBackfaces', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bRenderCurves', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bRenderIsoparams', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bRenderMeshEdges', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bRenderPoints', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bUseHiddenLights', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_bUsesAmbientAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesAnnotationAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesBackfaceAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesBackgroundAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesCurvesAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesHiddenLightsAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesIsoparmsAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesMeshEdgesAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_bUsesPointsAttr', 'bool', is_const=False)
    cls.add_instance_attribute('m_background_bitmap_filename', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_background_bottom_color', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_background_color', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_background_style', 'int', is_const=False)
    cls.add_instance_attribute('m_image_dpi', 'double', is_const=False)
    cls.add_instance_attribute('m_image_height', 'int', is_const=False)
    cls.add_instance_attribute('m_image_us', 'ON::unit_system', is_const=False)
    cls.add_instance_attribute('m_image_width', 'int', is_const=False)
    cls.add_instance_attribute('m_shadowmap_height', 'int', is_const=False)
    cls.add_instance_attribute('m_shadowmap_offset', 'double', is_const=False)
    cls.add_instance_attribute('m_shadowmap_style', 'int', is_const=False)
    cls.add_instance_attribute('m_shadowmap_width', 'int', is_const=False)
    return

def register_ON_3dmRevisionHistory_methods(root_module, cls):
    cls.add_constructor([param('ON_3dmRevisionHistory const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('CreateTimeIsSet', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True)
    cls.add_method('LastEditedTimeIsSet', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('NewRevision', 
                   'int', 
                   [])
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_create_time', 'tm', is_const=False)
    cls.add_instance_attribute('m_last_edit_time', 'tm', is_const=False)
    cls.add_instance_attribute('m_revision_count', 'int', is_const=False)
    cls.add_instance_attribute('m_sCreatedBy', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_sLastEditedBy', 'ON_wString', is_const=False)
    return

def register_ON_3dmSettings_methods(root_module, cls):
    cls.add_constructor([param('ON_3dmSettings const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_AnalysisMeshSettings', 'ON_MeshParameters', is_const=False)
    cls.add_instance_attribute('m_AnnotationSettings', 'ON_3dmAnnotationSettings', is_const=False)
    cls.add_instance_attribute('m_CustomRenderMeshSettings', 'ON_MeshParameters', is_const=False)
    cls.add_instance_attribute('m_GridDefaults', 'ON_3dmConstructionPlaneGridDefaults', is_const=False)
    cls.add_instance_attribute('m_IO_settings', 'ON_3dmIOSettings', is_const=False)
    cls.add_instance_attribute('m_ModelUnitsAndTolerances', 'ON_3dmUnitsAndTolerances', is_const=False)
    cls.add_instance_attribute('m_PageUnitsAndTolerances', 'ON_3dmUnitsAndTolerances', is_const=False)
    cls.add_instance_attribute('m_RenderMeshSettings', 'ON_MeshParameters', is_const=False)
    cls.add_instance_attribute('m_RenderSettings', 'ON_3dmRenderSettings', is_const=False)
    cls.add_instance_attribute('m_active_view_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_current_color', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_current_color_source', 'ON::object_color_source', is_const=False)
    cls.add_instance_attribute('m_current_dimstyle_index', 'int', is_const=False)
    cls.add_instance_attribute('m_current_font_index', 'int', is_const=False)
    cls.add_instance_attribute('m_current_layer_index', 'int', is_const=False)
    cls.add_instance_attribute('m_current_linetype_index', 'int', is_const=False)
    cls.add_instance_attribute('m_current_linetype_source', 'ON::object_linetype_source', is_const=False)
    cls.add_instance_attribute('m_current_material_index', 'int', is_const=False)
    cls.add_instance_attribute('m_current_material_source', 'ON::object_material_source', is_const=False)
    cls.add_instance_attribute('m_current_plot_color', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_current_plot_color_source', 'ON::plot_color_source', is_const=False)
    cls.add_instance_attribute('m_current_wire_density', 'int', is_const=False)
    cls.add_instance_attribute('m_earth_anchor_point', 'ON_EarthAnchorPoint', is_const=False)
    cls.add_instance_attribute('m_linetype_display_scale', 'double', is_const=False)
    cls.add_instance_attribute('m_model_URL', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_model_basepoint', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_named_cplanes', 'ON_ClassArray< ON_3dmConstructionPlane >', is_const=False)
    cls.add_instance_attribute('m_named_views', 'ON_ClassArray< ON_3dmView >', is_const=False)
    cls.add_instance_attribute('m_plugin_list', 'ON_ClassArray< ON_PlugInRef >', is_const=False)
    cls.add_instance_attribute('m_views', 'ON_ClassArray< ON_3dmView >', is_const=False)
    return

def register_ON_3dmUnitsAndTolerances_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmUnitsAndTolerances const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Scale', 
                   'double', 
                   [param('ON::unit_system', 'arg0')], 
                   is_const=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_absolute_tolerance', 'double', is_const=False)
    cls.add_instance_attribute('m_angle_tolerance', 'double', is_const=False)
    cls.add_instance_attribute('m_distance_display_mode', 'ON::distance_display_mode', is_const=False)
    cls.add_instance_attribute('m_distance_display_precision', 'int', is_const=False)
    cls.add_instance_attribute('m_relative_tolerance', 'double', is_const=False)
    cls.add_instance_attribute('m_unit_system', 'ON_UnitSystem', is_const=False)
    return

def register_ON_3dmView_methods(root_module, cls):
    cls.add_constructor([param('ON_3dmView const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('SetTargetPoint', 
                   'bool', 
                   [param('ON_3dPoint', 'target_point')])
    cls.add_method('TargetPoint', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bLockedProjection', 'bool', is_const=False)
    cls.add_instance_attribute('m_bShowConstructionAxes', 'bool', is_const=False)
    cls.add_instance_attribute('m_bShowConstructionGrid', 'bool', is_const=False)
    cls.add_instance_attribute('m_bShowWorldAxes', 'bool', is_const=False)
    cls.add_instance_attribute('m_clipping_planes', 'ON_SimpleArray< ON_ClippingPlaneInfo >', is_const=False)
    cls.add_instance_attribute('m_cplane', 'ON_3dmConstructionPlane', is_const=False)
    cls.add_instance_attribute('m_display_mode', 'ON::display_mode', is_const=False)
    cls.add_instance_attribute('m_display_mode_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_name', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_page_settings', 'ON_3dmPageSettings', is_const=False)
    cls.add_instance_attribute('m_position', 'ON_3dmViewPosition', is_const=False)
    cls.add_instance_attribute('m_target', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_trace_image', 'ON_3dmViewTraceImage', is_const=False)
    cls.add_instance_attribute('m_view_type', 'ON::view_type', is_const=False)
    cls.add_instance_attribute('m_vp', 'ON_Viewport', is_const=False)
    cls.add_instance_attribute('m_wallpaper_image', 'ON_3dmWallpaperImage', is_const=False)
    return

def register_ON_3dmViewPosition_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dmViewPosition const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bMaximized', 'ON_BOOL32', is_const=False)
    cls.add_instance_attribute('m_floating_viewport', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_wnd_bottom', 'double', is_const=False)
    cls.add_instance_attribute('m_wnd_left', 'double', is_const=False)
    cls.add_instance_attribute('m_wnd_right', 'double', is_const=False)
    cls.add_instance_attribute('m_wnd_top', 'double', is_const=False)
    return

def register_ON_3dmViewTraceImage_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_3dmViewTraceImage const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bFiltered', 'bool', is_const=False)
    cls.add_instance_attribute('m_bGrayScale', 'bool', is_const=False)
    cls.add_instance_attribute('m_bHidden', 'bool', is_const=False)
    cls.add_instance_attribute('m_bitmap_filename', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_height', 'double', is_const=False)
    cls.add_instance_attribute('m_plane', 'ON_Plane', is_const=False)
    cls.add_instance_attribute('m_width', 'double', is_const=False)
    return

def register_ON_3dmWallpaperImage_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_3dmWallpaperImage const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bGrayScale', 'bool', is_const=False)
    cls.add_instance_attribute('m_bHidden', 'bool', is_const=False)
    cls.add_instance_attribute('m_bitmap_filename', 'ON_wString', is_const=False)
    return

def register_ON_4dPoint_methods(root_module, cls):
    cls.add_inplace_numeric_operator('*=', param('double', u'right'))
    cls.add_inplace_numeric_operator('/=', param('double', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ON_4dPoint const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ON_4dPoint const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_4dPoint'], root_module['ON_4dPoint'], param('double', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ON_4dPoint'], root_module['ON_4dPoint'], param('double', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_4dPoint'], root_module['ON_4dPoint'], param('ON_4dPoint const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ON_4dPoint'], root_module['ON_4dPoint'], param('ON_4dPoint const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ON_4dPoint'], root_module['ON_4dPoint'], param('ON_Xform const &', u'right'))
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_4dPoint const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 'x'), param('double', 'y'), param('double', 'z'), param('double', 'w')])
    cls.add_constructor([param('ON_2dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3dPoint const &', 'arg0')])
    cls.add_constructor([param('ON_2dVector const &', 'arg0')])
    cls.add_constructor([param('ON_3dVector const &', 'arg0')])
    cls.add_constructor([param('double const *', 'arg0')])
    cls.add_constructor([param('ON_2fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_3fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_4fPoint const &', 'arg0')])
    cls.add_constructor([param('ON_2fVector const &', 'arg0')])
    cls.add_constructor([param('ON_3fVector const &', 'arg0')])
    cls.add_constructor([param('float const *', 'arg0')])
    cls.add_method('IsUnsetPoint', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinate', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumCoordinateIndex', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Normalize', 
                   'bool', 
                   [])
    cls.add_method('Set', 
                   'void', 
                   [param('double', 'x'), param('double', 'y'), param('double', 'z'), param('double', 'w')])
    cls.add_method('Transform', 
                   'void', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_instance_attribute('w', 'double', is_const=False)
    cls.add_instance_attribute('x', 'double', is_const=False)
    cls.add_instance_attribute('y', 'double', is_const=False)
    cls.add_instance_attribute('z', 'double', is_const=False)
    return

def register_ON_Base64EncodeStream_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_method('SetCallback', 
                   'bool', 
                   [param('ON_StreamCallbackFunction', 'callback_function'), param('void *', 'callback_context')])
    cls.add_method('CallbackFunction', 
                   'ON_StreamCallbackFunction', 
                   [], 
                   is_const=True)
    cls.add_method('CallbackContext', 
                   'void *', 
                   [], 
                   is_const=True)
    cls.add_method('Begin', 
                   'bool', 
                   [])
    cls.add_method('In', 
                   'bool', 
                   [param('ON__UINT64', 'in_buffer_size'), param('void const *', 'in_buffer')])
    cls.add_method('Out', 
                   'bool', 
                   [param('void *', 'callback_context'), param('ON__UINT32', 'out_buffer_size'), param('char const *', 'out_buffer')], 
                   is_virtual=True)
    cls.add_method('End', 
                   'bool', 
                   [])
    cls.add_method('InSize', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('OutSize', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('InCRC', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    cls.add_method('OutCRC', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    return

def register_ON_BezierCage_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'dim'), param('bool', 'is_rat'), param('int', 'order0'), param('int', 'order1'), param('int', 'order2')])
    cls.add_constructor([param('ON_BoundingBox const &', 'bbox'), param('int', 'order0'), param('int', 'order1'), param('int', 'order2')])
    cls.add_constructor([param('ON_3dPoint const *', 'box_corners'), param('int', 'order0'), param('int', 'order1'), param('int', 'order2')])
    cls.add_constructor([param('ON_BezierCage const &', 'src')])
    cls.add_method('CV', 
                   'double *', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k')], 
                   is_const=True)
    cls.add_method('CVSize', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('CVStyle', 
                   'ON::point_style', 
                   [], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('int', 'dim'), param('bool', 'is_rat'), param('int', 'order0'), param('int', 'order1'), param('int', 'order2')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'bbox'), param('int', 'order0'), param('int', 'order1'), param('int', 'order2')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_3dPoint const *', 'box_corners'), param('int', 'order0'), param('int', 'order1'), param('int', 'order2')])
    cls.add_method('Degree', 
                   'int', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Dimension', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Domain', 
                   'ON_Interval', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Evaluate', 
                   'bool', 
                   [param('double', 'r'), param('double', 's'), param('double', 't'), param('int', 'der_count'), param('int', 'v_stride'), param('double *', 'v')], 
                   is_const=True)
    cls.add_method('GetBBox', 
                   'bool', 
                   [param('double *', 'boxmin'), param('double *', 'boxmax'), param('int', 'bGrowBox', default_value='false')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k'), param('ON::point_style', 'arg3'), param('double *', 'arg4')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k'), param('ON_3dPoint &', 'arg3')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k'), param('ON_4dPoint &', 'arg3')], 
                   is_const=True)
    cls.add_method('IsRational', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsSingular', 
                   'bool', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('MakeNonRational', 
                   'bool', 
                   [])
    cls.add_method('MakeRational', 
                   'bool', 
                   [])
    cls.add_method('Order', 
                   'int', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'r'), param('double', 's'), param('double', 't')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'rst')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')])
    cls.add_method('ReserveCVCapacity', 
                   'bool', 
                   [param('int', 'cv_capacity')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'rotation_axis'), param('ON_3dPoint const &', 'rotation_center')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'rotation_angle'), param('ON_3dVector const &', 'rotation_axis'), param('ON_3dPoint const &', 'rotation_center')])
    cls.add_method('Scale', 
                   'bool', 
                   [param('double', 'scale_factor')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k'), param('ON::point_style', 'arg3'), param('double const *', 'arg4')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k'), param('ON_3dPoint const &', 'point')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k'), param('ON_4dPoint const &', 'hpoint')])
    cls.add_method('SetWeight', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k'), param('double', 'w')])
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'translation_vector')])
    cls.add_method('Weight', 
                   'double', 
                   [param('int', 'i'), param('int', 'j'), param('int', 'k')], 
                   is_const=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')], 
                   is_const=True)
    cls.add_method('ZeroCVs', 
                   'bool', 
                   [])
    cls.add_instance_attribute('m_cv', 'double *', is_const=False)
    cls.add_instance_attribute('m_cv_capacity', 'int', is_const=False)
    cls.add_instance_attribute('m_cv_stride', 'int [ 3 ]', is_const=False)
    cls.add_instance_attribute('m_dim', 'int', is_const=False)
    cls.add_instance_attribute('m_is_rat', 'bool', is_const=False)
    cls.add_instance_attribute('m_order', 'int [ 3 ]', is_const=False)
    return

def register_ON_BezierCurve_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'dim'), param('ON_BOOL32', 'bIsRational'), param('int', 'order')])
    cls.add_constructor([param('ON_BezierCurve const &', 'arg0')])
    cls.add_constructor([param('ON_PolynomialCurve const &', 'arg0')])
    cls.add_constructor([param('ON_2dPointArray const &', 'arg0')])
    cls.add_constructor([param('ON_3dPointArray const &', 'arg0')])
    cls.add_constructor([param('ON_4dPointArray const &', 'arg0')])
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('CV', 
                   'double *', 
                   [param('int', 'cv_index')], 
                   is_const=True)
    cls.add_method('CVCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('CVSize', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('CVStyle', 
                   'ON::point_style', 
                   [], 
                   is_const=True)
    cls.add_method('ChangeDimension', 
                   'bool', 
                   [param('int', 'desired_dimension')])
    cls.add_method('ChangeWeights', 
                   'bool', 
                   [param('int', 'i0'), param('double', 'w0'), param('int', 'i1'), param('double', 'w1')])
    cls.add_method('ControlPolygonLength', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('int', 'dim'), param('ON_BOOL32', 'bIsRational'), param('int', 'order')])
    cls.add_method('CurvatureAt', 
                   'ON_3dVector', 
                   [param('double', 't')], 
                   is_const=True)
    cls.add_method('Degree', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DerivativeAt', 
                   'ON_3dVector', 
                   [param('double', 't')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Dimension', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Domain', 
                   'ON_Interval', 
                   [], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Ev1Der', 
                   'bool', 
                   [param('double', 't'), param('ON_3dPoint &', 'point'), param('ON_3dVector &', 'first_derivative')], 
                   is_const=True)
    cls.add_method('Ev2Der', 
                   'bool', 
                   [param('double', 't'), param('ON_3dPoint &', 'point'), param('ON_3dVector &', 'first_derivative'), param('ON_3dVector &', 'second_derivative')], 
                   is_const=True)
    cls.add_method('EvCurvature', 
                   'bool', 
                   [param('double', 't'), param('ON_3dPoint &', 'point'), param('ON_3dVector &', 'tangent'), param('ON_3dVector &', 'kappa')], 
                   is_const=True)
    cls.add_method('EvPoint', 
                   'bool', 
                   [param('double', 't'), param('ON_3dPoint &', 'point')], 
                   is_const=True)
    cls.add_method('EvTangent', 
                   'bool', 
                   [param('double', 't'), param('ON_3dPoint &', 'point'), param('ON_3dVector &', 'tangent')], 
                   is_const=True)
    cls.add_method('Evaluate', 
                   'bool', 
                   [param('double', 't'), param('int', 'der_count'), param('int', 'v_stride'), param('double *', 'v')], 
                   is_const=True)
    cls.add_method('GetBBox', 
                   'bool', 
                   [param('double *', 'box_min'), param('double *', 'box_max'), param('int', 'bGrowBox', default_value='false')], 
                   is_const=True)
    cls.add_method('GetBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox &', 'bbox'), param('int', 'bGrowBox', default_value='false')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'cv_index'), param('ON::point_style', 'pointstyle'), param('double *', 'cv')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'cv_index'), param('ON_3dPoint &', 'point')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'cv_index'), param('ON_4dPoint &', 'point')], 
                   is_const=True)
    cls.add_method('GetClosestPoint', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('double *', 't'), param('double', 'maximum_distance', default_value='0.0'), param('ON_Interval const *', 'sub_domain', default_value='0')], 
                   is_const=True)
    cls.add_method('GetLocalClosestPoint', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('double', 'seed_parameter'), param('double *', 't'), param('ON_Interval const *', 'sub_domain', default_value='0')], 
                   is_const=True)
    cls.add_method('GetLocalCurveIntersection', 
                   'bool', 
                   [param('ON_BezierCurve const *', 'other_bezcrv'), param('double', 'this_seed_t'), param('double', 'other_seed_t'), param('double *', 'this_t'), param('double *', 'other_t'), param('ON_Interval const *', 'this_domain', default_value='0'), param('ON_Interval const *', 'other_domain', default_value='0')], 
                   is_const=True)
    cls.add_method('GetLocalSurfaceIntersection', 
                   'bool', 
                   [param('ON_BezierSurface const *', 'bezsrf'), param('double', 'seed_t'), param('double', 'seed_u'), param('double', 'seed_v'), param('double *', 't'), param('double *', 'u'), param('double *', 'v'), param('ON_Interval const *', 'tdomain', default_value='0'), param('ON_Interval const *', 'udomain', default_value='0'), param('ON_Interval const *', 'vdomain', default_value='0')], 
                   is_const=True)
    cls.add_method('GetNurbForm', 
                   'bool', 
                   [param('ON_NurbsCurve &', 'nurbs_curve')], 
                   is_const=True)
    cls.add_method('GetTightBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox &', 'tight_bbox'), param('int', 'bGrowBox', default_value='false'), param('ON_Xform const *', 'xform', default_value='0')], 
                   is_const=True)
    cls.add_method('IncreaseDegree', 
                   'bool', 
                   [param('int', 'desired_degree')])
    cls.add_method('IntersectCurve', 
                   'int', 
                   [param('ON_BezierCurve const *', 'bezierB'), param('ON_SimpleArray< ON_X_EVENT > &', 'x'), param('double', 'intersection_tolerance', default_value='0.0'), param('double', 'overlap_tolerance', default_value='0.0'), param('ON_Interval const *', 'bezierA_domain', default_value='0'), param('ON_Interval const *', 'bezierB_domain', default_value='0')], 
                   is_const=True)
    cls.add_method('IntersectSelf', 
                   'int', 
                   [param('ON_SimpleArray< ON_X_EVENT > &', 'x'), param('double', 'intersection_tolerance', default_value='0.0')], 
                   is_const=True)
    cls.add_method('IntersectSurface', 
                   'int', 
                   [param('ON_BezierSurface const *', 'bezsrfB'), param('ON_SimpleArray< ON_X_EVENT > &', 'x'), param('double', 'intersection_tolerance', default_value='0.0'), param('double', 'overlap_tolerance', default_value='0.0'), param('ON_Interval const *', 'bezierA_domain', default_value='0'), param('ON_Interval const *', 'bezsrfB_udomain', default_value='0'), param('ON_Interval const *', 'bezsrfB_vdomain', default_value='0')], 
                   is_const=True)
    cls.add_method('IsRational', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Loft', 
                   'bool', 
                   [param('ON_3dPointArray const &', 'points')])
    cls.add_method('Loft', 
                   'bool', 
                   [param('int', 'pt_dim'), param('int', 'pt_count'), param('int', 'pt_stride'), param('double const *', 'pt'), param('int', 't_stride'), param('double const *', 't')])
    cls.add_method('MakeNonRational', 
                   'bool', 
                   [])
    cls.add_method('MakeRational', 
                   'bool', 
                   [])
    cls.add_method('Order', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 't')], 
                   is_const=True)
    cls.add_method('Reparameterize', 
                   'bool', 
                   [param('double', 'c')])
    cls.add_method('Reparametrize', 
                   'bool', 
                   [param('double', 'arg0')])
    cls.add_method('ReserveCVCapacity', 
                   'bool', 
                   [param('int', 'desired_cv_capacity')])
    cls.add_method('Reverse', 
                   'bool', 
                   [])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'rotation_axis'), param('ON_3dPoint const &', 'rotation_center')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'rotation_angle'), param('ON_3dVector const &', 'rotation_axis'), param('ON_3dPoint const &', 'rotation_center')])
    cls.add_method('Scale', 
                   'bool', 
                   [param('double', 'scale_factor')])
    cls.add_method('ScaleConrolPoints', 
                   'bool', 
                   [param('int', 'i'), param('double', 'w')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'cv_index'), param('ON::point_style', 'pointstyle'), param('double const *', 'cv')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'cv_index'), param('ON_3dPoint const &', 'point')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'cv_index'), param('ON_4dPoint const &', 'point')])
    cls.add_method('SetWeight', 
                   'bool', 
                   [param('int', 'cv_index'), param('double', 'weight')])
    cls.add_method('Split', 
                   'bool', 
                   [param('double', 't'), param('ON_BezierCurve &', 'left_side'), param('ON_BezierCurve &', 'right_side')], 
                   is_const=True)
    cls.add_method('TangentAt', 
                   'ON_3dVector', 
                   [param('double', 't')], 
                   is_const=True)
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'translation_vector')])
    cls.add_method('Trim', 
                   'bool', 
                   [param('ON_Interval const &', 'interval')])
    cls.add_method('Weight', 
                   'double', 
                   [param('int', 'cv_index')], 
                   is_const=True)
    cls.add_method('ZeroCVs', 
                   'bool', 
                   [])
    cls.add_instance_attribute('m_cv', 'double *', is_const=False)
    cls.add_instance_attribute('m_cv_capacity', 'int', is_const=False)
    cls.add_instance_attribute('m_cv_stride', 'int', is_const=False)
    cls.add_instance_attribute('m_dim', 'int', is_const=False)
    cls.add_instance_attribute('m_is_rat', 'int', is_const=False)
    cls.add_instance_attribute('m_order', 'int', is_const=False)
    return

def register_ON_BezierSurface_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'dim'), param('int', 'is_rat'), param('int', 'order0'), param('int', 'order1')])
    cls.add_constructor([param('ON_BezierSurface const &', 'arg0')])
    cls.add_constructor([param('ON_PolynomialSurface const &', 'arg0')])
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('CV', 
                   'double *', 
                   [param('int', 'cv_index0'), param('int', 'cv_index1')], 
                   is_const=True)
    cls.add_method('CVSize', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('CVStyle', 
                   'ON::point_style', 
                   [], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('int', 'dim'), param('int', 'is_rat'), param('int', 'order0'), param('int', 'order1')])
    cls.add_method('Degree', 
                   'int', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Dimension', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Domain', 
                   'ON_Interval', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Evaluate', 
                   'bool', 
                   [param('double', 'arg0'), param('double', 'arg1'), param('int', 'arg2'), param('int', 'arg3'), param('double *', 'arg4')], 
                   is_const=True)
    cls.add_method('GetBBox', 
                   'bool', 
                   [param('double *', 'arg0'), param('double *', 'arg1'), param('int', 'bGrowBox', default_value='false')], 
                   is_const=True)
    cls.add_method('GetBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox &', 'bbox'), param('int', 'bGrowBox')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('ON::point_style', 'arg2'), param('double *', 'arg3')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('ON_3dPoint &', 'arg2')], 
                   is_const=True)
    cls.add_method('GetCV', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('ON_4dPoint &', 'arg2')], 
                   is_const=True)
    cls.add_method('GetClosestPoint', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('double *', 's'), param('double *', 't'), param('double', 'maximum_distance', default_value='0.0'), param('ON_Interval const *', 'sub_domain0', default_value='0'), param('ON_Interval const *', 'sub_domain1', default_value='0')], 
                   is_const=True)
    cls.add_method('GetLocalClosestPoint', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('double', 's_seed'), param('double', 't_seed'), param('double *', 's'), param('double *', 't'), param('ON_Interval const *', 'sub_domain0', default_value='0'), param('ON_Interval const *', 'sub_domain1', default_value='0')], 
                   is_const=True)
    cls.add_method('GetNurbForm', 
                   'bool', 
                   [param('ON_NurbsSurface &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsRational', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsSingular', 
                   'bool', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsoCurve', 
                   'ON_BezierCurve *', 
                   [param('int', 'dir'), param('double', 'c'), param('ON_BezierCurve *', 'iso', default_value='0')], 
                   is_const=True)
    cls.add_method('Loft', 
                   'bool', 
                   [param('ON_ClassArray< ON_BezierCurve > const &', 'curve_list')])
    cls.add_method('Loft', 
                   'bool', 
                   [param('int', 'count'), param('ON_BezierCurve const * const *', 'curve_list')])
    cls.add_method('MakeNonRational', 
                   'bool', 
                   [])
    cls.add_method('MakeRational', 
                   'bool', 
                   [])
    cls.add_method('Order', 
                   'int', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 's'), param('double', 't')], 
                   is_const=True)
    cls.add_method('ReserveCVCapacity', 
                   'bool', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'bool', 
                   [param('int', 'arg0')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'rotation_axis'), param('ON_3dPoint const &', 'rotation_center')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'rotation_angle'), param('ON_3dVector const &', 'rotation_axis'), param('ON_3dPoint const &', 'rotation_center')])
    cls.add_method('Scale', 
                   'bool', 
                   [param('double', 'scale_factor')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('ON::point_style', 'arg2'), param('double const *', 'arg3')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('ON_3dPoint const &', 'arg2')])
    cls.add_method('SetCV', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('ON_4dPoint const &', 'arg2')])
    cls.add_method('SetWeight', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('double', 'arg2')])
    cls.add_method('Split', 
                   'bool', 
                   [param('int', 'arg0'), param('double', 'arg1'), param('ON_BezierSurface &', 'arg2'), param('ON_BezierSurface &', 'arg3')], 
                   is_const=True)
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'translation_vector')])
    cls.add_method('Transpose', 
                   'bool', 
                   [])
    cls.add_method('Trim', 
                   'bool', 
                   [param('int', 'dir'), param('ON_Interval const &', 'domain')])
    cls.add_method('Weight', 
                   'double', 
                   [param('int', 'arg0'), param('int', 'arg1')], 
                   is_const=True)
    cls.add_method('ZeroCVs', 
                   'bool', 
                   [])
    cls.add_instance_attribute('m_cv', 'double *', is_const=False)
    cls.add_instance_attribute('m_cv_capacity', 'int', is_const=False)
    cls.add_instance_attribute('m_cv_stride', 'int [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_dim', 'int', is_const=False)
    cls.add_instance_attribute('m_is_rat', 'int', is_const=False)
    cls.add_instance_attribute('m_order', 'int [ 2 ]', is_const=False)
    return

def register_ON_BinaryArchive_methods(root_module, cls):
    cls.add_constructor([param('ON::archive_mode', 'arg0')])
    cls.add_method('Archive3dmVersion', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('ArchiveOpenNURBSVersion', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('ArchiveStartOffset', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('AtEnd', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    cls.add_method('BadCRCCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('BeginRead3dmBigChunk', 
                   'bool', 
                   [param('unsigned int *', 'arg0'), param('ON__INT64 *', 'arg1')])
    cls.add_method('BeginRead3dmBitmapTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmChunk', 
                   'bool', 
                   [param('unsigned int *', 'arg0'), param('int *', 'arg1')])
    cls.add_method('BeginRead3dmChunk', 
                   'bool', 
                   [param('unsigned int', 'expected_tcode'), param('int *', 'major_version'), param('int *', 'minor_version')])
    cls.add_method('BeginRead3dmDimStyleTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmFontTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmGroupTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmHatchPatternTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmHistoryRecordTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmInstanceDefinitionTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmLayerTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmLightTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmLinetypeTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmMaterialTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmObjectTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmTextureMappingTable', 
                   'bool', 
                   [])
    cls.add_method('BeginRead3dmUserTable', 
                   'bool', 
                   [param('ON_UUID &', 'plugin_id'), param('bool *', 'bLastSavedAsGoo'), param('int *', 'archive_3dm_version'), param('int *', 'archive_opennurbs_version')])
    cls.add_method('BeginRead3dmUserTable', 
                   'bool', 
                   [param('ON_UUID &', 'arg0')])
    cls.add_method('BeginReadDictionary', 
                   'bool', 
                   [param('ON_UUID *', 'dictionary_id'), param('unsigned int *', 'version'), param('ON_wString &', 'dictionary_name')])
    cls.add_method('BeginReadDictionaryEntry', 
                   'int', 
                   [param('int *', 'de_type'), param('ON_wString &', 'entry_name')])
    cls.add_method('BeginWrite3dmBigChunk', 
                   'bool', 
                   [param('ON__UINT32', 'typecode'), param('ON__INT64', 'value')])
    cls.add_method('BeginWrite3dmBitmapTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmChunk', 
                   'bool', 
                   [param('unsigned int', 'arg0'), param('int', 'arg1')])
    cls.add_method('BeginWrite3dmChunk', 
                   'bool', 
                   [param('unsigned int', 'tcode'), param('int', 'major_version'), param('int', 'minor_version')])
    cls.add_method('BeginWrite3dmDimStyleTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmFontTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmGroupTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmHatchPatternTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmHistoryRecordTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmInstanceDefinitionTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmLayerTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmLightTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmLinetypeTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmMaterialTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmObjectTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmTextureMappingTable', 
                   'bool', 
                   [])
    cls.add_method('BeginWrite3dmUserTable', 
                   'bool', 
                   [param('ON_UUID const &', 'plugin_id'), param('bool', 'bSavingGoo'), param('int', 'goo_3dm_version'), param('int', 'goo_opennurbs_version')])
    cls.add_method('BeginWrite3dmUserTable', 
                   'bool', 
                   [param('ON_UUID const &', 'arg0')])
    cls.add_method('BeginWriteDictionary', 
                   'bool', 
                   [param('ON_UUID', 'dictionary_id'), param('unsigned int', 'version'), param('wchar_t const *', 'dictionary_name')])
    cls.add_method('BeginWriteDictionaryEntry', 
                   'bool', 
                   [param('int', 'de_type'), param('wchar_t const *', 'entry_name')])
    cls.add_method('BigSeekBackward', 
                   'bool', 
                   [param('ON__UINT64', 'offset')])
    cls.add_method('BigSeekForward', 
                   'bool', 
                   [param('ON__UINT64', 'offset')])
    cls.add_method('BigSeekFromCurrentPosition', 
                   'bool', 
                   [param('ON__INT64', 'offset')])
    cls.add_method('BigSeekFromStart', 
                   'bool', 
                   [param('ON__UINT64', 'offset')])
    cls.add_method('CurrentArchiveVersion', 
                   'int', 
                   [], 
                   is_static=True)
    cls.add_method('CurrentPosition', 
                   'size_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    cls.add_method('Dump3dmChunk', 
                   'unsigned int', 
                   [param('ON_TextLog &', 'text_log'), param('int', 'recursion_depth', default_value='0')])
    cls.add_method('EnableCRCCalculation', 
                   'bool', 
                   [param('bool', 'bEnable')])
    cls.add_method('EnableSave3dmAnalysisMeshes', 
                   'bool', 
                   [param('ON_BOOL32', 'arg0', default_value='true')])
    cls.add_method('EnableSave3dmRenderMeshes', 
                   'bool', 
                   [param('ON_BOOL32', 'arg0', default_value='true')])
    cls.add_method('EnableSaveUserData', 
                   'bool', 
                   [param('ON_BOOL32', 'arg0', default_value='true')])
    cls.add_method('EndRead3dmBitmapTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmChunk', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmChunk', 
                   'bool', 
                   [param('bool', 'bSupressPartiallyReadChunkWarning')])
    cls.add_method('EndRead3dmDimStyleTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmFontTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmGroupTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmHatchPatternTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmHistoryRecordTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmInstanceDefinitionTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmLayerTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmLightTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmLinetypeTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmMaterialTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmObjectTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmTextureMappingTable', 
                   'bool', 
                   [])
    cls.add_method('EndRead3dmUserTable', 
                   'bool', 
                   [])
    cls.add_method('EndReadDictionary', 
                   'bool', 
                   [])
    cls.add_method('EndReadDictionaryEntry', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmBitmapTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmChunk', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmDimStyleTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmFontTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmGroupTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmHatchPatternTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmHistoryRecordTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmInstanceDefinitionTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmLayerTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmLightTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmLinetypeTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmMaterialTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmObjectTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmTextureMappingTable', 
                   'bool', 
                   [])
    cls.add_method('EndWrite3dmUserTable', 
                   'bool', 
                   [])
    cls.add_method('EndWriteDictionary', 
                   'bool', 
                   [])
    cls.add_method('EndWriteDictionaryEntry', 
                   'bool', 
                   [])
    cls.add_method('Endian', 
                   'ON::endian', 
                   [], 
                   is_const=True)
    cls.add_method('FindTableInDamagedArchive', 
                   'bool', 
                   [param('unsigned int', 'tcode_table'), param('unsigned int', 'tcode_record'), param('ON_UUID', 'class_uuid'), param('int', 'min_length_data')])
    cls.add_method('GetCurrentChunk', 
                   'int', 
                   [param('ON_3DM_CHUNK &', 'chunk')], 
                   is_const=True)
    cls.add_method('GetCurrentChunk', 
                   'int', 
                   [param('ON_3DM_BIG_CHUNK &', 'big_chunk')], 
                   is_const=True)
    cls.add_method('ON_TypecodeParse', 
                   'char *', 
                   [param('unsigned int', 'tcode'), param('char *', 'typecode_name'), param('size_t', 'max_length')], 
                   is_static=True)
    cls.add_method('PeekAt3dmBigChunkType', 
                   'bool', 
                   [param('ON__UINT32 *', 'typecode'), param('ON__INT64 *', 'big_value')])
    cls.add_method('PeekAt3dmChunkType', 
                   'bool', 
                   [param('unsigned int *', 'arg0'), param('int *', 'arg1')])
    cls.add_method('Read3dmAnonymousUserTable', 
                   'bool', 
                   [param('int', 'archive_3dm_version'), param('int', 'archive_opennurbs_version'), param('ON_3dmGoo &', 'goo')])
    cls.add_method('Read3dmAnonymousUserTable', 
                   'bool', 
                   [param('ON_3dmGoo &', 'arg0')])
    cls.add_method('Read3dmBitmap', 
                   'int', 
                   [param('ON_Bitmap * *', 'arg0')])
    cls.add_method('Read3dmChunkVersion', 
                   'bool', 
                   [param('int *', 'arg0'), param('int *', 'arg1')])
    cls.add_method('Read3dmDimStyle', 
                   'int', 
                   [param('ON_DimStyle * *', 'arg0')])
    cls.add_method('Read3dmEndMark', 
                   'bool', 
                   [param('size_t *', 'arg0')])
    cls.add_method('Read3dmFont', 
                   'int', 
                   [param('ON_Font * *', 'arg0')])
    cls.add_method('Read3dmGoo', 
                   'bool', 
                   [param('ON_3dmGoo &', 'arg0')])
    cls.add_method('Read3dmGroup', 
                   'int', 
                   [param('ON_Group * *', 'arg0')])
    cls.add_method('Read3dmHatchPattern', 
                   'int', 
                   [param('ON_HatchPattern * *', 'arg0')])
    cls.add_method('Read3dmHistoryRecord', 
                   'int', 
                   [param('ON_HistoryRecord * &', 'arg0')])
    cls.add_method('Read3dmInstanceDefinition', 
                   'int', 
                   [param('ON_InstanceDefinition * *', 'arg0')])
    cls.add_method('Read3dmLayer', 
                   'int', 
                   [param('ON_Layer * *', 'arg0')])
    cls.add_method('Read3dmLight', 
                   'int', 
                   [param('ON_Light * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('Read3dmLinetype', 
                   'int', 
                   [param('ON_Linetype * *', 'arg0')])
    cls.add_method('Read3dmMaterial', 
                   'int', 
                   [param('ON_Material * *', 'arg0')])
    cls.add_method('Read3dmObject', 
                   'int', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1'), param('unsigned int', 'arg2', default_value='0')])
    cls.add_method('Read3dmProperties', 
                   'bool', 
                   [param('ON_3dmProperties &', 'arg0')])
    cls.add_method('Read3dmSettings', 
                   'bool', 
                   [param('ON_3dmSettings &', 'arg0')])
    cls.add_method('Read3dmStartSection', 
                   'bool', 
                   [param('int *', 'version'), param('ON_String &', 'sStartSectionComment')])
    cls.add_method('Read3dmTextureMapping', 
                   'int', 
                   [param('ON_TextureMapping * *', 'arg0')])
    cls.add_method('ReadArc', 
                   'bool', 
                   [param('ON_Arc &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< bool > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< char > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< short int > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< int > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< float > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< double > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_Color > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2dPoint > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3dPoint > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_4dPoint > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2dVector > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3dVector > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_Xform > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2fPoint > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3fPoint > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_4fPoint > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2fVector > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3fVector > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_UUID > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_UuidIndex > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_SurfaceCurvature > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_String > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_wString > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_DisplayMaterialRef > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_LinetypeSegment > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_MappingChannel > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_MaterialRef > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_MappingRef > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_ObjRef > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_ObjRef_IRefID > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_ClippingPlaneInfo > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_ObjectArray< ON_Layer > &', 'arg0')])
    cls.add_method('ReadArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_Layer * > &', 'arg0')])
    cls.add_method('ReadBigInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('ON__INT64 *', 'arg1')])
    cls.add_method('ReadBigInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('ON__UINT64 *', 'arg1')])
    cls.add_method('ReadBigInt', 
                   'bool', 
                   [param('ON__INT64 *', 'arg0')])
    cls.add_method('ReadBigInt', 
                   'bool', 
                   [param('ON__UINT64 *', 'arg0')])
    cls.add_method('ReadBigSize', 
                   'bool', 
                   [param('size_t *', 'arg0')])
    cls.add_method('ReadBigTime', 
                   'bool', 
                   [param('time_t *', 'arg0')])
    cls.add_method('ReadBool', 
                   'bool', 
                   [param('bool *', 'arg0')])
    cls.add_method('ReadBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox &', 'arg0')])
    cls.add_method('ReadBuffer', 
                   'ON__UINT64', 
                   [param('ON__UINT64', 'sizeof_buffer'), param('void *', 'buffer')])
    cls.add_method('ReadByte', 
                   'bool', 
                   [param('size_t', 'arg0'), param('void *', 'arg1')])
    cls.add_method('ReadChar', 
                   'bool', 
                   [param('size_t', 'arg0'), param('char *', 'arg1')])
    cls.add_method('ReadChar', 
                   'bool', 
                   [param('size_t', 'arg0'), param('unsigned char *', 'arg1')])
    cls.add_method('ReadChar', 
                   'bool', 
                   [param('char *', 'arg0')])
    cls.add_method('ReadChar', 
                   'bool', 
                   [param('unsigned char *', 'arg0')])
    cls.add_method('ReadCircle', 
                   'bool', 
                   [param('ON_Circle &', 'arg0')])
    cls.add_method('ReadColor', 
                   'bool', 
                   [param('ON_Color &', 'arg0')])
    cls.add_method('ReadComponentIndex', 
                   'bool', 
                   [param('ON_COMPONENT_INDEX &', 'arg0')])
    cls.add_method('ReadCompressedBuffer', 
                   'bool', 
                   [param('size_t', 'sizeof__outbuffer'), param('void *', 'outbuffer'), param('int *', 'bFailedCRC')])
    cls.add_method('ReadCompressedBufferSize', 
                   'bool', 
                   [param('size_t *', 'sizeof__outbuffer')])
    cls.add_method('ReadDisplayMaterialRef', 
                   'bool', 
                   [param('ON_DisplayMaterialRef &', 'arg0')])
    cls.add_method('ReadDouble', 
                   'bool', 
                   [param('size_t', 'arg0'), param('double *', 'arg1')])
    cls.add_method('ReadDouble', 
                   'bool', 
                   [param('double *', 'arg0')])
    cls.add_method('ReadFloat', 
                   'bool', 
                   [param('size_t', 'arg0'), param('float *', 'arg1')])
    cls.add_method('ReadFloat', 
                   'bool', 
                   [param('float *', 'arg0')])
    cls.add_method('ReadInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('int *', 'arg1')])
    cls.add_method('ReadInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('unsigned int *', 'arg1')])
    cls.add_method('ReadInt', 
                   'bool', 
                   [param('int *', 'arg0')])
    cls.add_method('ReadInt', 
                   'bool', 
                   [param('unsigned int *', 'arg0')])
    cls.add_method('ReadInterval', 
                   'bool', 
                   [param('ON_Interval &', 'arg0')])
    cls.add_method('ReadLine', 
                   'bool', 
                   [param('ON_Line &', 'arg0')])
    cls.add_method('ReadLinetypeSegment', 
                   'bool', 
                   [param('ON_LinetypeSegment &', 'arg0')])
    cls.add_method('ReadLong', 
                   'bool', 
                   [param('size_t', 'arg0'), param('long int *', 'arg1')])
    cls.add_method('ReadLong', 
                   'bool', 
                   [param('size_t', 'arg0'), param('long unsigned int *', 'arg1')])
    cls.add_method('ReadLong', 
                   'bool', 
                   [param('long int *', 'arg0')])
    cls.add_method('ReadLong', 
                   'bool', 
                   [param('long unsigned int *', 'arg0')])
    cls.add_method('ReadMode', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('ReadObject', 
                   'int', 
                   [param('ON_Object * *', 'ppObject')])
    cls.add_method('ReadObject', 
                   'int', 
                   [param('ON_Object &', 'object')])
    cls.add_method('ReadObjectUserData', 
                   'bool', 
                   [param('ON_Object &', 'object')])
    cls.add_method('ReadPlane', 
                   'bool', 
                   [param('ON_Plane &', 'arg0')])
    cls.add_method('ReadPlaneEquation', 
                   'bool', 
                   [param('ON_PlaneEquation &', 'arg0')])
    cls.add_method('ReadPoint', 
                   'bool', 
                   [param('ON_2dPoint &', 'arg0')])
    cls.add_method('ReadPoint', 
                   'bool', 
                   [param('ON_3dPoint &', 'arg0')])
    cls.add_method('ReadPoint', 
                   'bool', 
                   [param('ON_4dPoint &', 'arg0')])
    cls.add_method('ReadShort', 
                   'bool', 
                   [param('size_t', 'arg0'), param('short int *', 'arg1')])
    cls.add_method('ReadShort', 
                   'bool', 
                   [param('size_t', 'arg0'), param('short unsigned int *', 'arg1')])
    cls.add_method('ReadShort', 
                   'bool', 
                   [param('short int *', 'arg0')])
    cls.add_method('ReadShort', 
                   'bool', 
                   [param('short unsigned int *', 'arg0')])
    cls.add_method('ReadSize', 
                   'bool', 
                   [param('size_t *', 'arg0')])
    cls.add_method('ReadString', 
                   'bool', 
                   [param('size_t', 'str_array_count'), param('char *', 'str_array')])
    cls.add_method('ReadString', 
                   'bool', 
                   [param('size_t', 'str_array_count'), param('unsigned char *', 'str_array')])
    cls.add_method('ReadString', 
                   'bool', 
                   [param('size_t', 'str_array_count'), param('short unsigned int *', 'str_array')])
    cls.add_method('ReadString', 
                   'bool', 
                   [param('ON_String &', 'sUTF8')])
    cls.add_method('ReadString', 
                   'bool', 
                   [param('ON_wString &', 's')])
    cls.add_method('ReadStringSize', 
                   'bool', 
                   [param('size_t *', 'str_array_count')])
    cls.add_method('ReadStringUTF16ElementCount', 
                   'bool', 
                   [param('size_t *', 'string_utf16_element_count')])
    cls.add_method('ReadStringUTF8ElementCount', 
                   'bool', 
                   [param('size_t *', 'string_utf8_element_count')])
    cls.add_method('ReadTime', 
                   'bool', 
                   [param('tm &', 'arg0')])
    cls.add_method('ReadUuid', 
                   'bool', 
                   [param('ON_UUID &', 'arg0')])
    cls.add_method('ReadV1_TCODE_ANNOTATION', 
                   'bool', 
                   [param('unsigned int', 'arg0'), param('ON_Object * *', 'arg1'), param('ON_3dmObjectAttributes *', 'arg2')])
    cls.add_method('ReadV1_TCODE_LEGACY_CRV', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadV1_TCODE_LEGACY_FAC', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadV1_TCODE_LEGACY_SHL', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadV1_TCODE_MESH_OBJECT', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadV1_TCODE_RHINOIO_OBJECT_BREP', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadV1_TCODE_RHINOIO_OBJECT_NURBS_CURVE', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadV1_TCODE_RHINOIO_OBJECT_NURBS_SURFACE', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadV1_TCODE_RH_POINT', 
                   'bool', 
                   [param('ON_Object * *', 'arg0'), param('ON_3dmObjectAttributes *', 'arg1')])
    cls.add_method('ReadVector', 
                   'bool', 
                   [param('ON_2dVector &', 'arg0')])
    cls.add_method('ReadVector', 
                   'bool', 
                   [param('ON_3dVector &', 'arg0')])
    cls.add_method('ReadXform', 
                   'bool', 
                   [param('ON_Xform &', 'arg0')])
    cls.add_method('Save3dmAnalysisMeshes', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Save3dmRenderMeshes', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('SaveUserData', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Seek3dmChunkFromCurrentPosition', 
                   'bool', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('Seek3dmChunkFromStart', 
                   'bool', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('SeekFromCurrentPosition', 
                   'bool', 
                   [param('int', 'arg0')], 
                   is_pure_virtual=True, is_virtual=True)
    cls.add_method('SeekFromStart', 
                   'bool', 
                   [param('size_t', 'arg0')], 
                   is_pure_virtual=True, is_virtual=True)
    cls.add_method('SizeofChunkLength', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('ToggleByteOrder', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('void const *', 'arg2'), param('void *', 'arg3')], 
                   is_static=True)
    cls.add_method('TypecodeName', 
                   'char const *', 
                   [param('unsigned int', 'tcode')], 
                   is_static=True)
    cls.add_method('Write3dmAnonymousUserTable', 
                   'bool', 
                   [param('ON_3dmGoo const &', 'arg0')])
    cls.add_method('Write3dmAnonymousUserTableRecord', 
                   'bool', 
                   [param('ON_UUID const &', 'plugin_id'), param('int', 'goo_3dm_version'), param('int', 'goo_opennurbs_version'), param('ON_3dmGoo const &', 'goo')])
    cls.add_method('Write3dmBitmap', 
                   'bool', 
                   [param('ON_Bitmap const &', 'arg0')])
    cls.add_method('Write3dmChunkVersion', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('Write3dmDimStyle', 
                   'bool', 
                   [param('ON_DimStyle const &', 'arg0')])
    cls.add_method('Write3dmEndMark', 
                   'bool', 
                   [])
    cls.add_method('Write3dmFont', 
                   'bool', 
                   [param('ON_Font const &', 'arg0')])
    cls.add_method('Write3dmGoo', 
                   'bool', 
                   [param('ON_3dmGoo const &', 'arg0')])
    cls.add_method('Write3dmGroup', 
                   'bool', 
                   [param('ON_Group const &', 'arg0')])
    cls.add_method('Write3dmHatchPattern', 
                   'bool', 
                   [param('ON_HatchPattern const &', 'arg0')])
    cls.add_method('Write3dmHistoryRecord', 
                   'bool', 
                   [param('ON_HistoryRecord const &', 'arg0')])
    cls.add_method('Write3dmInstanceDefinition', 
                   'bool', 
                   [param('ON_InstanceDefinition const &', 'arg0')])
    cls.add_method('Write3dmLayer', 
                   'bool', 
                   [param('ON_Layer const &', 'arg0')])
    cls.add_method('Write3dmLight', 
                   'bool', 
                   [param('ON_Light const &', 'arg0'), param('ON_3dmObjectAttributes const *', 'arg1')])
    cls.add_method('Write3dmLinetype', 
                   'bool', 
                   [param('ON_Linetype const &', 'arg0')])
    cls.add_method('Write3dmMaterial', 
                   'bool', 
                   [param('ON_Material const &', 'arg0')])
    cls.add_method('Write3dmObject', 
                   'bool', 
                   [param('ON_Object const &', 'arg0'), param('ON_3dmObjectAttributes const *', 'arg1')])
    cls.add_method('Write3dmProperties', 
                   'bool', 
                   [param('ON_3dmProperties const &', 'arg0')])
    cls.add_method('Write3dmSettings', 
                   'bool', 
                   [param('ON_3dmSettings const &', 'arg0')])
    cls.add_method('Write3dmStartSection', 
                   'bool', 
                   [param('int', 'version'), param('char const *', 'sStartSectionComment')])
    cls.add_method('Write3dmTextureMapping', 
                   'bool', 
                   [param('ON_TextureMapping const &', 'arg0')])
    cls.add_method('WriteArc', 
                   'bool', 
                   [param('ON_Arc const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< bool > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< char > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< short int > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< int > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< float > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< double > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_Color > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2dPoint > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3dPoint > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_4dPoint > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2dVector > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3dVector > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2fPoint > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3fPoint > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_4fPoint > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2fVector > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3fVector > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_Xform > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_UUID > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_UuidIndex > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_SurfaceCurvature > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_String > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_wString > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_DisplayMaterialRef > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_LinetypeSegment > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_MappingChannel > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_MaterialRef > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_MappingRef > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_ClassArray< ON_ObjRef > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_ObjRef_IRefID > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('ON_SimpleArray< ON_ClippingPlaneInfo > const &', 'arg0')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('int', 'count'), param('ON_Layer const *', 'arg1')])
    cls.add_method('WriteArray', 
                   'bool', 
                   [param('int', 'count'), param('ON_Layer const * const *', 'arg1')])
    cls.add_method('WriteBigInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('ON__INT64 const *', 'arg1')])
    cls.add_method('WriteBigInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('ON__UINT64 const *', 'arg1')])
    cls.add_method('WriteBigInt', 
                   'bool', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('WriteBigInt', 
                   'bool', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('WriteBigSize', 
                   'bool', 
                   [param('size_t', 'arg0')])
    cls.add_method('WriteBigTime', 
                   'bool', 
                   [param('time_t', 'arg0')])
    cls.add_method('WriteBool', 
                   'bool', 
                   [param('bool', 'arg0')])
    cls.add_method('WriteBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'arg0')])
    cls.add_method('WriteByte', 
                   'bool', 
                   [param('size_t', 'arg0'), param('void const *', 'arg1')])
    cls.add_method('WriteChar', 
                   'bool', 
                   [param('size_t', 'arg0'), param('char const *', 'arg1')])
    cls.add_method('WriteChar', 
                   'bool', 
                   [param('size_t', 'arg0'), param('unsigned char const *', 'arg1')])
    cls.add_method('WriteChar', 
                   'bool', 
                   [param('char', 'arg0')])
    cls.add_method('WriteChar', 
                   'bool', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('WriteCircle', 
                   'bool', 
                   [param('ON_Circle const &', 'arg0')])
    cls.add_method('WriteColor', 
                   'bool', 
                   [param('ON_Color const &', 'arg0')])
    cls.add_method('WriteComponentIndex', 
                   'bool', 
                   [param('ON_COMPONENT_INDEX const &', 'arg0')])
    cls.add_method('WriteCompressedBuffer', 
                   'bool', 
                   [param('size_t', 'sizeof__inbuffer'), param('void const *', 'inbuffer')])
    cls.add_method('WriteDisplayMaterialRef', 
                   'bool', 
                   [param('ON_DisplayMaterialRef const &', 'arg0')])
    cls.add_method('WriteDouble', 
                   'bool', 
                   [param('size_t', 'arg0'), param('double const *', 'arg1')])
    cls.add_method('WriteDouble', 
                   'bool', 
                   [param('double', 'arg0')])
    cls.add_method('WriteFloat', 
                   'bool', 
                   [param('size_t', 'arg0'), param('float const *', 'arg1')])
    cls.add_method('WriteFloat', 
                   'bool', 
                   [param('float', 'arg0')])
    cls.add_method('WriteInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('int const *', 'arg1')])
    cls.add_method('WriteInt', 
                   'bool', 
                   [param('size_t', 'arg0'), param('unsigned int const *', 'arg1')])
    cls.add_method('WriteInt', 
                   'bool', 
                   [param('int', 'arg0')])
    cls.add_method('WriteInt', 
                   'bool', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('WriteInterval', 
                   'bool', 
                   [param('ON_Interval const &', 'arg0')])
    cls.add_method('WriteLine', 
                   'bool', 
                   [param('ON_Line const &', 'arg0')])
    cls.add_method('WriteLinetypeSegment', 
                   'bool', 
                   [param('ON_LinetypeSegment const &', 'arg0')])
    cls.add_method('WriteLong', 
                   'bool', 
                   [param('size_t', 'arg0'), param('long int const *', 'arg1')])
    cls.add_method('WriteLong', 
                   'bool', 
                   [param('size_t', 'arg0'), param('long unsigned int const *', 'arg1')])
    cls.add_method('WriteLong', 
                   'bool', 
                   [param('long int', 'arg0')])
    cls.add_method('WriteLong', 
                   'bool', 
                   [param('long unsigned int', 'arg0')])
    cls.add_method('WriteMode', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('WriteObject', 
                   'bool', 
                   [param('ON_Object const *', 'arg0')])
    cls.add_method('WriteObject', 
                   'bool', 
                   [param('ON_Object const &', 'arg0')])
    cls.add_method('WriteObjectUserData', 
                   'bool', 
                   [param('ON_Object const &', 'object')])
    cls.add_method('WritePlane', 
                   'bool', 
                   [param('ON_Plane const &', 'arg0')])
    cls.add_method('WritePlaneEquation', 
                   'bool', 
                   [param('ON_PlaneEquation const &', 'arg0')])
    cls.add_method('WritePoint', 
                   'bool', 
                   [param('ON_2dPoint const &', 'arg0')])
    cls.add_method('WritePoint', 
                   'bool', 
                   [param('ON_3dPoint const &', 'arg0')])
    cls.add_method('WritePoint', 
                   'bool', 
                   [param('ON_4dPoint const &', 'arg0')])
    cls.add_method('WriteShort', 
                   'bool', 
                   [param('size_t', 'arg0'), param('short int const *', 'arg1')])
    cls.add_method('WriteShort', 
                   'bool', 
                   [param('size_t', 'arg0'), param('short unsigned int const *', 'arg1')])
    cls.add_method('WriteShort', 
                   'bool', 
                   [param('short int', 'arg0')])
    cls.add_method('WriteShort', 
                   'bool', 
                   [param('short unsigned int', 'arg0')])
    cls.add_method('WriteSize', 
                   'bool', 
                   [param('size_t', 'arg0')])
    cls.add_method('WriteString', 
                   'bool', 
                   [param('char const *', 'sUTF8')])
    cls.add_method('WriteString', 
                   'bool', 
                   [param('unsigned char const *', 'sUTF8')])
    cls.add_method('WriteString', 
                   'bool', 
                   [param('short unsigned int const *', 'sUTF16')])
    cls.add_method('WriteString', 
                   'bool', 
                   [param('ON_String const &', 'sUTF8')])
    cls.add_method('WriteString', 
                   'bool', 
                   [param('ON_wString const &', 's')])
    cls.add_method('WriteTime', 
                   'bool', 
                   [param('tm const &', 'arg0')])
    cls.add_method('WriteUuid', 
                   'bool', 
                   [param('ON_UUID const &', 'arg0')])
    cls.add_method('WriteVector', 
                   'bool', 
                   [param('ON_2dVector const &', 'arg0')])
    cls.add_method('WriteVector', 
                   'bool', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_method('WriteXform', 
                   'bool', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('ErrorMessageMask', 
                   'unsigned int', 
                   [], 
                   is_const=True, visibility='protected')
    cls.add_method('Flush', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    cls.add_method('LoadUserDataApplication', 
                   'int', 
                   [param('ON_UUID', 'application_id')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('MaskReadError', 
                   'bool', 
                   [param('ON__UINT64', 'sizeof_request'), param('ON__UINT64', 'sizeof_read')], 
                   is_const=True, visibility='protected')
    cls.add_method('Read', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void *', 'arg1')], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    cls.add_method('SetArchive3dmVersion', 
                   'bool', 
                   [param('int', 'arg0')], 
                   visibility='protected')
    cls.add_method('Write', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void const *', 'arg1')], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    return

def register_ON_BinaryArchiveBuffer_methods(root_module, cls):
    cls.add_constructor([param('ON::archive_mode', 'arg0'), param('ON_Buffer *', 'buffer')])
    cls.add_method('SetBuffer', 
                   'bool', 
                   [param('ON_Buffer *', 'buffer')])
    cls.add_method('Buffer', 
                   'ON_Buffer *', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentPosition', 
                   'size_t', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('SeekFromCurrentPosition', 
                   'bool', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('SeekFromStart', 
                   'bool', 
                   [param('size_t', 'arg0')], 
                   is_virtual=True)
    cls.add_method('AtEnd', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('SeekFromEnd', 
                   'bool', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('Read', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void *', 'arg1')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('Write', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void const *', 'arg1')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('Flush', 
                   'bool', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_ON_BinaryFile_methods(root_module, cls):
    cls.add_constructor([param('ON::archive_mode', 'arg0')])
    cls.add_constructor([param('ON::archive_mode', 'arg0'), param('FILE *', 'fp')])
    cls.add_method('CurrentPosition', 
                   'size_t', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('SeekFromCurrentPosition', 
                   'bool', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('SeekFromStart', 
                   'bool', 
                   [param('size_t', 'arg0')], 
                   is_virtual=True)
    cls.add_method('AtEnd', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('SeekFromEnd', 
                   'bool', 
                   [param('int', 'arg0')])
    cls.add_method('EnableMemoryBuffer', 
                   'void', 
                   [param('int', 'arg0', default_value='16384')])
    cls.add_method('Read', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void *', 'arg1')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('Write', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void const *', 'arg1')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('Flush', 
                   'bool', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_ON_BoundingBox_methods(root_module, cls):
    cls.add_constructor([param('ON_BoundingBox const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dPoint const &', 'arg0'), param('ON_3dPoint const &', 'arg1')])
    cls.add_method('Area', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Center', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('ClosestPoint', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint const &', 'test_point')], 
                   is_const=True)
    cls.add_method('Corner', 
                   'ON_3dPoint', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Diagonal', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('FarPoint', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('GetClosestPoint', 
                   'int', 
                   [param('ON_Line const &', 'arg0'), param('ON_3dPoint &', 'arg1'), param('double *', 'arg2'), param('double *', 'arg3')], 
                   is_const=True)
    cls.add_method('GetClosestPoint', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'arg0'), param('ON_3dPoint &', 'arg1'), param('ON_3dPoint &', 'arg2')], 
                   is_const=True)
    cls.add_method('GetCorners', 
                   'bool', 
                   [param('ON_3dPointArray &', 'box_corners')], 
                   is_const=True)
    cls.add_method('GetCorners', 
                   'bool', 
                   [param('ON_3dPoint *', 'box_corners')], 
                   is_const=True)
    cls.add_method('GetFarPoint', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'arg0'), param('ON_3dPoint &', 'arg1'), param('ON_3dPoint &', 'arg2')], 
                   is_const=True)
    cls.add_method('Includes', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'other'), param('bool', 'bProperSubSet', default_value='false')], 
                   is_const=True)
    cls.add_method('Intersection', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'other_bbox')])
    cls.add_method('Intersection', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'bbox_A'), param('ON_BoundingBox const &', 'bbox_B')])
    cls.add_method('Intersection', 
                   'bool', 
                   [param('ON_Line const &', 'arg0'), param('double *', 'arg1', default_value='0'), param('double *', 'arg2', default_value='0')], 
                   is_const=True)
    cls.add_method('IsDegenerate', 
                   'int', 
                   [param('double', 'tolerance', default_value='-1.2343210123432100841968750719648103327947880256e+308')], 
                   is_const=True)
    cls.add_method('IsDisjoint', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'other_bbox')], 
                   is_const=True)
    cls.add_method('IsFartherThan', 
                   'bool', 
                   [param('double', 'd'), param('ON_3dPoint const &', 'P')], 
                   is_const=True)
    cls.add_method('IsFartherThan', 
                   'bool', 
                   [param('double', 'd'), param('ON_Line const &', 'line')], 
                   is_const=True)
    cls.add_method('IsFartherThan', 
                   'bool', 
                   [param('double', 'd'), param('ON_Plane const &', 'plane')], 
                   is_const=True)
    cls.add_method('IsFartherThan', 
                   'bool', 
                   [param('double', 'd'), param('ON_PlaneEquation const &', 'plane_equation')], 
                   is_const=True)
    cls.add_method('IsFartherThan', 
                   'bool', 
                   [param('double', 'd'), param('ON_BoundingBox const &', 'other')], 
                   is_const=True)
    cls.add_method('IsPointIn', 
                   'bool', 
                   [param('ON_3dPoint const &', 'test_point'), param('int', 'bStrictlyIn', default_value='false')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsVisible', 
                   'int', 
                   [param('ON_Xform const &', 'bbox2c')], 
                   is_const=True)
    cls.add_method('Max', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumDistanceTo', 
                   'double', 
                   [param('ON_3dPoint const &', 'P')], 
                   is_const=True)
    cls.add_method('MaximumDistanceTo', 
                   'double', 
                   [param('ON_BoundingBox const &', 'other')], 
                   is_const=True)
    cls.add_method('MaximumDistanceTo', 
                   'double', 
                   [param('ON_Line const &', 'line')], 
                   is_const=True)
    cls.add_method('MaximumDistanceTo', 
                   'double', 
                   [param('ON_Plane const &', 'plane')], 
                   is_const=True)
    cls.add_method('MaximumDistanceTo', 
                   'double', 
                   [param('ON_PlaneEquation const &', 'plane_equation')], 
                   is_const=True)
    cls.add_method('Min', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumDistanceTo', 
                   'double', 
                   [param('ON_3dPoint const &', 'P')], 
                   is_const=True)
    cls.add_method('MinimumDistanceTo', 
                   'double', 
                   [param('ON_BoundingBox const &', 'other')], 
                   is_const=True)
    cls.add_method('MinimumDistanceTo', 
                   'double', 
                   [param('ON_Line const &', 'line')], 
                   is_const=True)
    cls.add_method('MinimumDistanceTo', 
                   'double', 
                   [param('ON_Plane const &', 'plane')], 
                   is_const=True)
    cls.add_method('MinimumDistanceTo', 
                   'double', 
                   [param('ON_PlaneEquation const &', 'plane_equation')], 
                   is_const=True)
    cls.add_method('Set', 
                   'bool', 
                   [param('int', 'dim'), param('int', 'is_rat'), param('int', 'count'), param('int', 'stride'), param('double const *', 'point_array'), param('int', 'bGrowBox', default_value='false')])
    cls.add_method('Set', 
                   'bool', 
                   [param('ON_3dPoint const &', 'point'), param('int', 'bGrowBox', default_value='false')])
    cls.add_method('Set', 
                   'bool', 
                   [param('ON_SimpleArray< ON_4dPoint > const &', 'point_array'), param('int', 'bGrowBox', default_value='false')])
    cls.add_method('Set', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3dPoint > const &', 'point_array'), param('int', 'bGrowBox', default_value='false')])
    cls.add_method('Set', 
                   'bool', 
                   [param('ON_SimpleArray< ON_2dPoint > const &', 'point_array'), param('int', 'bGrowBox', default_value='false')])
    cls.add_method('SwapCoordinates', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('Tolerance', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Union', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'arg0')])
    cls.add_method('Union', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'arg0'), param('ON_BoundingBox const &', 'arg1')])
    cls.add_method('Volume', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_static_attribute('EmptyBoundingBox', 'ON_BoundingBox const', is_const=True)
    cls.add_instance_attribute('m_max', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_min', 'ON_3dPoint', is_const=False)
    return

def register_ON_Box_methods(root_module, cls):
    cls.add_constructor([param('ON_Box const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_BoundingBox const &', 'bbox')])
    cls.add_method('Area', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('Center', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'bool', 
                   [param('ON_3dPoint', 'point'), param('double *', 'r'), param('double *', 's'), param('double *', 't')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'test_point')], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'bbox')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('GetCorners', 
                   'bool', 
                   [param('ON_3dPoint *', 'corners')], 
                   is_const=True)
    cls.add_method('GetCorners', 
                   'bool', 
                   [param('ON_SimpleArray< ON_3dPoint > &', 'corners')], 
                   is_const=True)
    cls.add_method('IsDegenerate', 
                   'int', 
                   [param('double', 'tolerance', default_value='-1.2343210123432100841968750719648103327947880256e+308')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'r'), param('double', 's'), param('double', 't')], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle_radians'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle_radians'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_method('Volume', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_instance_attribute('dx', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('dy', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('dz', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('plane', 'ON_Plane', is_const=False)
    return

def register_ON_BrepRegionTopology_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_BrepRegionTopology const &', 'src')])
    cls.add_method('Brep', 
                   'ON_Brep *', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_FS', 'ON_BrepFaceSideArray', is_const=False)
    cls.add_instance_attribute('m_R', 'ON_BrepRegionArray', is_const=False)
    return

def register_ON_BrepTrimPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_BrepTrimPoint const &', 'arg0')])
    cls.add_instance_attribute('e', 'double', is_const=False)
    cls.add_instance_attribute('p', 'ON_2dPoint', is_const=False)
    cls.add_instance_attribute('t', 'double', is_const=False)
    return

def register_ON_Buffer_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_Buffer const &', 'src')])
    cls.add_method('AtEnd', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('CRC32', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('ChangeSize', 
                   'bool', 
                   [param('ON__UINT64', 'buffer_size')])
    cls.add_method('ClearLastError', 
                   'void', 
                   [])
    cls.add_method('Compact', 
                   'bool', 
                   [])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_Buffer const &', 'a'), param('ON_Buffer const &', 'b')], 
                   is_static=True)
    cls.add_method('Compress', 
                   'bool', 
                   [param('ON_Buffer &', 'compressed_buffer')], 
                   is_const=True)
    cls.add_method('CurrentPosition', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('ErrorHandler', 
                   'ON_Buffer_ErrorHandler', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog const *', 'text_log')], 
                   is_const=True)
    cls.add_method('LastError', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON__UINT64', 
                   [param('ON__UINT64', 'size'), param('void *', 'buffer')])
    cls.add_method('ReadFromBinaryArchive', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Seek', 
                   'bool', 
                   [param('ON__INT64', 'offset'), param('int', 'origin')])
    cls.add_method('SeekFromCurrentPosition', 
                   'bool', 
                   [param('ON__INT64', 'offset')])
    cls.add_method('SeekFromEnd', 
                   'bool', 
                   [param('ON__INT64', 'offset')])
    cls.add_method('SeekFromStart', 
                   'bool', 
                   [param('ON__INT64', 'offset')])
    cls.add_method('SetErrorHandler', 
                   'void', 
                   [param('ON_Buffer_ErrorHandler', 'error_handler')])
    cls.add_method('Size', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('Uncompress', 
                   'bool', 
                   [param('ON_Buffer &', 'uncompressed_buffer')], 
                   is_const=True)
    cls.add_method('Write', 
                   'ON__UINT64', 
                   [param('ON__UINT64', 'size'), param('void const *', 'buffer')])
    cls.add_method('WriteToBinaryArchive', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    return

def register_ON_BumpFunction_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_constructor([param('ON_BumpFunction const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Evaluate', 
                   'void', 
                   [param('double', 's'), param('double', 't'), param('int', 'der_count'), param('double *', 'value')], 
                   is_const=True)
    cls.add_method('EvaluateHelperLinearBump', 
                   'void', 
                   [param('double', 't'), param('double', 'dt'), param('int', 'der_count'), param('double *', 'value')], 
                   is_const=True)
    cls.add_method('EvaluateHelperQuinticBump', 
                   'void', 
                   [param('double', 't'), param('double', 'dt'), param('int', 'der_count'), param('double *', 'value')], 
                   is_const=True)
    cls.add_method('ValueAt', 
                   'double', 
                   [param('double', 's'), param('double', 't')], 
                   is_const=True)
    cls.add_instance_attribute('m_a', 'double', is_const=False)
    cls.add_instance_attribute('m_point', 'ON_2dPoint', is_const=False)
    cls.add_instance_attribute('m_sx', 'double [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_sy', 'double [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_type', 'int [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_x0', 'double', is_const=False)
    cls.add_instance_attribute('m_y0', 'double', is_const=False)
    return

def register_ON_COMPONENT_INDEX_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>')
    cls.add_binary_comparison_operator('>=')
    cls.add_constructor([param('ON_COMPONENT_INDEX const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_COMPONENT_INDEX::TYPE', 'type'), param('int', 'index')])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_COMPONENT_INDEX const *', 'a'), param('ON_COMPONENT_INDEX const *', 'b')], 
                   is_static=True)
    cls.add_method('IsAnnotationComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsBrepComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsExtrusionComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsExtrusionPathComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsExtrusionProfileComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsExtrusionWallComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsExtrusionWallEdgeComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsExtrusionWallSurfaceComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsGroupMemberComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsIDefComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsMeshComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsPointCloudComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsPolyCurveComponentIndex', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsSet', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Set', 
                   'void', 
                   [param('ON_COMPONENT_INDEX::TYPE', 'type'), param('int', 'index')])
    cls.add_method('Type', 
                   'ON_COMPONENT_INDEX::TYPE', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('UnSet', 
                   'void', 
                   [])
    cls.add_instance_attribute('m_index', 'int', is_const=False)
    cls.add_instance_attribute('m_type', 'ON_COMPONENT_INDEX::TYPE', is_const=False)
    return

def register_ON_CheckSum_methods(root_module, cls):
    cls.add_constructor([param('ON_CheckSum const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('CheckBuffer', 
                   'bool', 
                   [param('size_t', 'size'), param('void const *', 'buffer')], 
                   is_const=True)
    cls.add_method('CheckFile', 
                   'bool', 
                   [param('FILE *', 'fp'), param('bool', 'bSkipTimeCheck', default_value='false')], 
                   is_const=True)
    cls.add_method('CheckFile', 
                   'bool', 
                   [param('wchar_t const *', 'filename'), param('bool', 'bSkipTimeCheck', default_value='false')], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsSet', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('SetBufferCheckSum', 
                   'bool', 
                   [param('size_t', 'size'), param('void const *', 'buffer'), param('time_t', 'time')])
    cls.add_method('SetFileCheckSum', 
                   'bool', 
                   [param('FILE *', 'fp')])
    cls.add_method('SetFileCheckSum', 
                   'bool', 
                   [param('wchar_t const *', 'filename')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_static_attribute('UnsetCheckSum', 'ON_CheckSum const', is_const=True)
    cls.add_instance_attribute('m_crc', 'ON__UINT32 [ 8 ]', is_const=False)
    cls.add_instance_attribute('m_size', 'size_t', is_const=False)
    cls.add_instance_attribute('m_time', 'time_t', is_const=False)
    return

def register_ON_Circle_methods(root_module, cls):
    cls.add_constructor([param('ON_Circle const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_Plane const &', 'plane'), param('double', 'radius')])
    cls.add_constructor([param('ON_3dPoint const &', 'center'), param('double', 'radius')])
    cls.add_constructor([param('ON_Plane const &', 'plane'), param('ON_3dPoint const &', 'center'), param('double', 'radius')])
    cls.add_constructor([param('ON_2dPoint const &', 'P'), param('ON_2dPoint const &', 'Q'), param('ON_2dPoint const &', 'R')])
    cls.add_constructor([param('ON_3dPoint const &', 'P'), param('ON_3dPoint const &', 'Q'), param('ON_3dPoint const &', 'R')])
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('Center', 
                   'ON_3dPoint const &', 
                   [], 
                   is_const=True)
    cls.add_method('Circumference', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'bool', 
                   [param('ON_3dPoint const &', 'point'), param('double *', 't')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint const &', 'point')], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_Plane const &', 'plane'), param('double', 'radius')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_3dPoint const &', 'center'), param('double', 'radius')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_Plane const &', 'plane'), param('ON_3dPoint const &', 'center'), param('double', 'radius')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_2dPoint const &', 'P'), param('ON_2dPoint const &', 'Q'), param('ON_2dPoint const &', 'R')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dPoint const &', 'Q'), param('ON_3dPoint const &', 'R')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_2dPoint const &', 'P'), param('ON_2dVector const &', 'tangent_at_P'), param('ON_2dPoint const &', 'Q')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dVector const &', 'tangent_at_P'), param('ON_3dPoint const &', 'Q')])
    cls.add_method('DerivativeAt', 
                   'ON_3dVector', 
                   [param('int', 'arg0'), param('double', 'arg1')], 
                   is_const=True)
    cls.add_method('Diameter', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('EquationAt', 
                   'double', 
                   [param('ON_2dPoint const &', 'plane_point')], 
                   is_const=True)
    cls.add_method('GetNurbForm', 
                   'int', 
                   [param('ON_NurbsCurve &', 'nurbs_curve')], 
                   is_const=True)
    cls.add_method('GetNurbFormParameterFromRadian', 
                   'bool', 
                   [param('double', 'circle_radians_parameter'), param('double *', 'nurbs_parameter')], 
                   is_const=True)
    cls.add_method('GetRadianFromNurbFormParameter', 
                   'bool', 
                   [param('double', 'nurbs_parameter'), param('double *', 'circle_radians_parameter')], 
                   is_const=True)
    cls.add_method('GetTightBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox &', 'tight_bbox'), param('int', 'bGrowBox', default_value='false'), param('ON_Xform const *', 'xform', default_value='0')], 
                   is_const=True)
    cls.add_method('GradientAt', 
                   'ON_2dVector', 
                   [param('ON_2dPoint const &', 'plane_point')], 
                   is_const=True)
    cls.add_method('IsInPlane', 
                   'bool', 
                   [param('ON_Plane const &', 'arg0'), param('double', 'arg1', default_value='2.3283064365386962890625e-10')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Normal', 
                   'ON_3dVector const &', 
                   [], 
                   is_const=True)
    cls.add_method('Plane', 
                   'ON_Plane const &', 
                   [], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'arg0')], 
                   is_const=True)
    cls.add_method('Radius', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Reverse', 
                   'bool', 
                   [])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle_in_radians'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle_in_radians'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('TangentAt', 
                   'ON_3dVector', 
                   [param('double', 'arg0')], 
                   is_const=True)
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'delta')])
    cls.add_instance_attribute('plane', 'ON_Plane', is_const=False)
    cls.add_instance_attribute('radius', 'double', is_const=False)
    return

def register_ON_ClassArray__ONX_Model_Object_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ONX_Model_Object > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ONX_Model_Object *', 
                   [])
    cls.add_method('First', 
                   'ONX_Model_Object const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_Object *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ONX_Model_Object *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ONX_Model_Object *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ONX_Model_Object *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ONX_Model_Object const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_Object const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_Object const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_Object const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ONX_Model_Object *', 
                   [])
    cls.add_method('Last', 
                   'ONX_Model_Object const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ONX_Model_Object &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ONX_Model_Object const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ONX_Model_Object const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ONX_Model_Object const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ONX_Model_Object const *', 'key'), param('int ( * ) ( ONX_Model_Object const *, ONX_Model_Object const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ONX_Model_Object const *', 'key'), param('int ( * ) ( ONX_Model_Object const *, ONX_Model_Object const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ONX_Model_Object const *', 'key'), param('int ( * ) ( ONX_Model_Object const *, ONX_Model_Object const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ONX_Model_Object const *, ONX_Model_Object const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ONX_Model_Object const *, ONX_Model_Object const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ONX_Model_Object const *, ONX_Model_Object const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ONX_Model_Object const *, ONX_Model_Object const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ONX_Model_Object *', 
                   [param('ONX_Model_Object *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ONX_Model_Object *', 
                   [])
    cls.add_method('Array', 
                   'ONX_Model_Object const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ONX_Model_Object *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ONX_Model_Object *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ONX_Model_Object *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ONX_Model_Object *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ONX_Model_Object &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ONX_Model_RenderLight_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ONX_Model_RenderLight > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ONX_Model_RenderLight *', 
                   [])
    cls.add_method('First', 
                   'ONX_Model_RenderLight const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_RenderLight *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ONX_Model_RenderLight *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ONX_Model_RenderLight *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ONX_Model_RenderLight *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ONX_Model_RenderLight const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_RenderLight const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_RenderLight const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_RenderLight const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ONX_Model_RenderLight *', 
                   [])
    cls.add_method('Last', 
                   'ONX_Model_RenderLight const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ONX_Model_RenderLight &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ONX_Model_RenderLight const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ONX_Model_RenderLight const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ONX_Model_RenderLight const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ONX_Model_RenderLight const *', 'key'), param('int ( * ) ( ONX_Model_RenderLight const *, ONX_Model_RenderLight const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ONX_Model_RenderLight const *', 'key'), param('int ( * ) ( ONX_Model_RenderLight const *, ONX_Model_RenderLight const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ONX_Model_RenderLight const *', 'key'), param('int ( * ) ( ONX_Model_RenderLight const *, ONX_Model_RenderLight const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ONX_Model_RenderLight const *, ONX_Model_RenderLight const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ONX_Model_RenderLight const *, ONX_Model_RenderLight const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ONX_Model_RenderLight const *, ONX_Model_RenderLight const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ONX_Model_RenderLight const *, ONX_Model_RenderLight const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ONX_Model_RenderLight *', 
                   [param('ONX_Model_RenderLight *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ONX_Model_RenderLight *', 
                   [])
    cls.add_method('Array', 
                   'ONX_Model_RenderLight const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ONX_Model_RenderLight *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ONX_Model_RenderLight *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ONX_Model_RenderLight *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ONX_Model_RenderLight *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ONX_Model_RenderLight &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ONX_Model_UserData_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ONX_Model_UserData > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ONX_Model_UserData *', 
                   [])
    cls.add_method('First', 
                   'ONX_Model_UserData const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_UserData *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ONX_Model_UserData *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ONX_Model_UserData *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ONX_Model_UserData *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ONX_Model_UserData const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_UserData const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_UserData const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ONX_Model_UserData const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ONX_Model_UserData *', 
                   [])
    cls.add_method('Last', 
                   'ONX_Model_UserData const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ONX_Model_UserData &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ONX_Model_UserData const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ONX_Model_UserData const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ONX_Model_UserData const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ONX_Model_UserData const *', 'key'), param('int ( * ) ( ONX_Model_UserData const *, ONX_Model_UserData const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ONX_Model_UserData const *', 'key'), param('int ( * ) ( ONX_Model_UserData const *, ONX_Model_UserData const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ONX_Model_UserData const *', 'key'), param('int ( * ) ( ONX_Model_UserData const *, ONX_Model_UserData const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ONX_Model_UserData const *, ONX_Model_UserData const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ONX_Model_UserData const *, ONX_Model_UserData const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ONX_Model_UserData const *, ONX_Model_UserData const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ONX_Model_UserData const *, ONX_Model_UserData const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ONX_Model_UserData *', 
                   [param('ONX_Model_UserData *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ONX_Model_UserData *', 
                   [])
    cls.add_method('Array', 
                   'ONX_Model_UserData const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ONX_Model_UserData *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ONX_Model_UserData *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ONX_Model_UserData *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ONX_Model_UserData *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ONX_Model_UserData &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_3dmConstructionPlane_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_3dmConstructionPlane > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_3dmConstructionPlane *', 
                   [])
    cls.add_method('First', 
                   'ON_3dmConstructionPlane const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmConstructionPlane *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_3dmConstructionPlane *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_3dmConstructionPlane *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_3dmConstructionPlane *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_3dmConstructionPlane const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmConstructionPlane const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmConstructionPlane const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmConstructionPlane const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_3dmConstructionPlane *', 
                   [])
    cls.add_method('Last', 
                   'ON_3dmConstructionPlane const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_3dmConstructionPlane &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_3dmConstructionPlane const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_3dmConstructionPlane const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_3dmConstructionPlane const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3dmConstructionPlane const *', 'key'), param('int ( * ) ( ON_3dmConstructionPlane const *, ON_3dmConstructionPlane const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dmConstructionPlane const *', 'key'), param('int ( * ) ( ON_3dmConstructionPlane const *, ON_3dmConstructionPlane const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dmConstructionPlane const *', 'key'), param('int ( * ) ( ON_3dmConstructionPlane const *, ON_3dmConstructionPlane const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dmConstructionPlane const *, ON_3dmConstructionPlane const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dmConstructionPlane const *, ON_3dmConstructionPlane const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_3dmConstructionPlane const *, ON_3dmConstructionPlane const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_3dmConstructionPlane const *, ON_3dmConstructionPlane const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_3dmConstructionPlane *', 
                   [param('ON_3dmConstructionPlane *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_3dmConstructionPlane *', 
                   [])
    cls.add_method('Array', 
                   'ON_3dmConstructionPlane const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_3dmConstructionPlane *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dmConstructionPlane *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dmConstructionPlane *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_3dmConstructionPlane *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_3dmConstructionPlane &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_3dmView_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_3dmView > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_3dmView *', 
                   [])
    cls.add_method('First', 
                   'ON_3dmView const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmView *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_3dmView *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_3dmView *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_3dmView *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_3dmView const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmView const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmView const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dmView const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_3dmView *', 
                   [])
    cls.add_method('Last', 
                   'ON_3dmView const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_3dmView &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_3dmView const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_3dmView const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_3dmView const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3dmView const *', 'key'), param('int ( * ) ( ON_3dmView const *, ON_3dmView const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dmView const *', 'key'), param('int ( * ) ( ON_3dmView const *, ON_3dmView const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dmView const *', 'key'), param('int ( * ) ( ON_3dmView const *, ON_3dmView const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dmView const *, ON_3dmView const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dmView const *, ON_3dmView const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_3dmView const *, ON_3dmView const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_3dmView const *, ON_3dmView const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_3dmView *', 
                   [param('ON_3dmView *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_3dmView *', 
                   [])
    cls.add_method('Array', 
                   'ON_3dmView const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_3dmView *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dmView *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dmView *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_3dmView *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_3dmView &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_BrepEdge_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_BrepEdge > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepEdge *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepEdge const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepEdge *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepEdge *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepEdge *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepEdge *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepEdge const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepEdge const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepEdge const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepEdge const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepEdge *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepEdge const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepEdge &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepEdge const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepEdge const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepEdge const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepEdge const *', 'key'), param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepEdge const *', 'key'), param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepEdge const *', 'key'), param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepEdge *', 
                   [param('ON_BrepEdge *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepEdge *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepEdge const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepEdge *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepEdge *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepEdge *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_BrepEdge *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_BrepEdge &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_BrepFace_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_BrepFace > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepFace *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFace *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepFace *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepFace *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepFace *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepFace const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFace const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFace const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFace const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepFace *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepFace &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepFace const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepFace const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepFace const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepFace const *', 'key'), param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepFace const *', 'key'), param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepFace const *', 'key'), param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepFace *', 
                   [param('ON_BrepFace *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepFace *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepFace *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepFace *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepFace *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_BrepFace *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_BrepFace &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_BrepFaceSide_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_BrepFaceSide > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepFaceSide *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepFaceSide const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFaceSide *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepFaceSide *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepFaceSide *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepFaceSide *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepFaceSide const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFaceSide const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFaceSide const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepFaceSide const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepFaceSide *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepFaceSide const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepFaceSide &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepFaceSide const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepFaceSide const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepFaceSide const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepFaceSide const *', 'key'), param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepFaceSide const *', 'key'), param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepFaceSide const *', 'key'), param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepFaceSide *', 
                   [param('ON_BrepFaceSide *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepFaceSide *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepFaceSide const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepFaceSide *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepFaceSide *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepFaceSide *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_BrepFaceSide *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_BrepFaceSide &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_BrepLoop_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_BrepLoop > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepLoop *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepLoop const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepLoop *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepLoop *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepLoop *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepLoop *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepLoop const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepLoop const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepLoop const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepLoop const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepLoop *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepLoop const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepLoop &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepLoop const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepLoop const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepLoop const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepLoop const *', 'key'), param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepLoop const *', 'key'), param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepLoop const *', 'key'), param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepLoop *', 
                   [param('ON_BrepLoop *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepLoop *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepLoop const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepLoop *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepLoop *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepLoop *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_BrepLoop *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_BrepLoop &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_BrepRegion_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_BrepRegion > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepRegion *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepRegion const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepRegion *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepRegion *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepRegion *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepRegion *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepRegion const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepRegion const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepRegion const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepRegion const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepRegion *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepRegion const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepRegion &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepRegion const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepRegion const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepRegion const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepRegion const *', 'key'), param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepRegion const *', 'key'), param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepRegion const *', 'key'), param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepRegion *', 
                   [param('ON_BrepRegion *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepRegion *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepRegion const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepRegion *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepRegion *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepRegion *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_BrepRegion *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_BrepRegion &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_BrepTrim_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_BrepTrim > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepTrim *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepTrim const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrim *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrim *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrim *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrim *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrim const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrim const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrim const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrim const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepTrim *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepTrim const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepTrim &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepTrim const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepTrim const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepTrim const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepTrim const *', 'key'), param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepTrim const *', 'key'), param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepTrim const *', 'key'), param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepTrim *', 
                   [param('ON_BrepTrim *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepTrim *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepTrim const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepTrim *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepTrim *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepTrim *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_BrepTrim *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_BrepTrim &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_BrepVertex_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_BrepVertex > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepVertex *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepVertex const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepVertex *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepVertex *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepVertex *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepVertex *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepVertex const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepVertex const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepVertex const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepVertex const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepVertex *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepVertex const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepVertex &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepVertex const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepVertex const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepVertex const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepVertex const *', 'key'), param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepVertex const *', 'key'), param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepVertex const *', 'key'), param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepVertex *', 
                   [param('ON_BrepVertex *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepVertex *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepVertex const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepVertex *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepVertex *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepVertex *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_BrepVertex *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_BrepVertex &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_CurveProxyHistory_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_CurveProxyHistory > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_CurveProxyHistory *', 
                   [])
    cls.add_method('First', 
                   'ON_CurveProxyHistory const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_CurveProxyHistory *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_CurveProxyHistory *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_CurveProxyHistory *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_CurveProxyHistory *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_CurveProxyHistory const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_CurveProxyHistory const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_CurveProxyHistory const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_CurveProxyHistory const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_CurveProxyHistory *', 
                   [])
    cls.add_method('Last', 
                   'ON_CurveProxyHistory const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_CurveProxyHistory &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_CurveProxyHistory const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_CurveProxyHistory const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_CurveProxyHistory const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_CurveProxyHistory const *', 'key'), param('int ( * ) ( ON_CurveProxyHistory const *, ON_CurveProxyHistory const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_CurveProxyHistory const *', 'key'), param('int ( * ) ( ON_CurveProxyHistory const *, ON_CurveProxyHistory const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_CurveProxyHistory const *', 'key'), param('int ( * ) ( ON_CurveProxyHistory const *, ON_CurveProxyHistory const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_CurveProxyHistory const *, ON_CurveProxyHistory const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_CurveProxyHistory const *, ON_CurveProxyHistory const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_CurveProxyHistory const *, ON_CurveProxyHistory const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_CurveProxyHistory const *, ON_CurveProxyHistory const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_CurveProxyHistory *', 
                   [param('ON_CurveProxyHistory *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_CurveProxyHistory *', 
                   [])
    cls.add_method('Array', 
                   'ON_CurveProxyHistory const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_CurveProxyHistory *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_CurveProxyHistory *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_CurveProxyHistory *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_CurveProxyHistory *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_CurveProxyHistory &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_DimStyle_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_DimStyle > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_DimStyle *', 
                   [])
    cls.add_method('First', 
                   'ON_DimStyle const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DimStyle *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_DimStyle *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_DimStyle *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_DimStyle *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_DimStyle const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DimStyle const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DimStyle const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DimStyle const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_DimStyle *', 
                   [])
    cls.add_method('Last', 
                   'ON_DimStyle const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_DimStyle &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_DimStyle const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_DimStyle const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_DimStyle const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_DimStyle const *', 'key'), param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_DimStyle const *', 'key'), param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_DimStyle const *', 'key'), param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_DimStyle *', 
                   [param('ON_DimStyle *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_DimStyle *', 
                   [])
    cls.add_method('Array', 
                   'ON_DimStyle const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_DimStyle *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_DimStyle *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_DimStyle *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_DimStyle *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_DimStyle &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_Font_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_Font > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Font *', 
                   [])
    cls.add_method('First', 
                   'ON_Font const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Font *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Font *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Font *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Font *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Font const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Font const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Font const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Font const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Font *', 
                   [])
    cls.add_method('Last', 
                   'ON_Font const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Font &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Font const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Font const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Font const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Font const *', 'key'), param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Font const *', 'key'), param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Font const *', 'key'), param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Font const *, ON_Font const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Font *', 
                   [param('ON_Font *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Font *', 
                   [])
    cls.add_method('Array', 
                   'ON_Font const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Font *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Font *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Font *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_Font *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_Font &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_Group_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_Group > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Group *', 
                   [])
    cls.add_method('First', 
                   'ON_Group const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Group *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Group *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Group *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Group *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Group const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Group const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Group const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Group const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Group *', 
                   [])
    cls.add_method('Last', 
                   'ON_Group const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Group &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Group const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Group const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Group const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Group const *', 'key'), param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Group const *', 'key'), param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Group const *', 'key'), param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Group const *, ON_Group const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Group *', 
                   [param('ON_Group *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Group *', 
                   [])
    cls.add_method('Array', 
                   'ON_Group const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Group *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Group *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Group *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_Group *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_Group &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_HatchLine_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_HatchLine > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_HatchLine *', 
                   [])
    cls.add_method('First', 
                   'ON_HatchLine const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLine *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_HatchLine *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_HatchLine *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_HatchLine *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_HatchLine const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLine const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLine const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLine const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_HatchLine *', 
                   [])
    cls.add_method('Last', 
                   'ON_HatchLine const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_HatchLine &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_HatchLine const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_HatchLine const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_HatchLine const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_HatchLine const *', 'key'), param('int ( * ) ( ON_HatchLine const *, ON_HatchLine const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HatchLine const *', 'key'), param('int ( * ) ( ON_HatchLine const *, ON_HatchLine const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HatchLine const *', 'key'), param('int ( * ) ( ON_HatchLine const *, ON_HatchLine const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchLine const *, ON_HatchLine const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchLine const *, ON_HatchLine const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HatchLine const *, ON_HatchLine const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HatchLine const *, ON_HatchLine const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_HatchLine *', 
                   [param('ON_HatchLine *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_HatchLine *', 
                   [])
    cls.add_method('Array', 
                   'ON_HatchLine const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_HatchLine *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HatchLine *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HatchLine *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_HatchLine *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_HatchLine &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_HatchPattern_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_HatchPattern > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_HatchPattern *', 
                   [])
    cls.add_method('First', 
                   'ON_HatchPattern const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchPattern *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_HatchPattern *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_HatchPattern *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_HatchPattern *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_HatchPattern const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchPattern const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchPattern const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchPattern const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_HatchPattern *', 
                   [])
    cls.add_method('Last', 
                   'ON_HatchPattern const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_HatchPattern &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_HatchPattern const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_HatchPattern const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_HatchPattern const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_HatchPattern const *', 'key'), param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HatchPattern const *', 'key'), param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HatchPattern const *', 'key'), param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_HatchPattern *', 
                   [param('ON_HatchPattern *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_HatchPattern *', 
                   [])
    cls.add_method('Array', 
                   'ON_HatchPattern const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_HatchPattern *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HatchPattern *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HatchPattern *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_HatchPattern *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_HatchPattern &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_InstanceDefinition_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_InstanceDefinition > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_InstanceDefinition *', 
                   [])
    cls.add_method('First', 
                   'ON_InstanceDefinition const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_InstanceDefinition *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_InstanceDefinition *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_InstanceDefinition *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_InstanceDefinition *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_InstanceDefinition const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_InstanceDefinition const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_InstanceDefinition const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_InstanceDefinition const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_InstanceDefinition *', 
                   [])
    cls.add_method('Last', 
                   'ON_InstanceDefinition const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_InstanceDefinition &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_InstanceDefinition const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_InstanceDefinition const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_InstanceDefinition const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_InstanceDefinition const *', 'key'), param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_InstanceDefinition const *', 'key'), param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_InstanceDefinition const *', 'key'), param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_InstanceDefinition *', 
                   [param('ON_InstanceDefinition *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_InstanceDefinition *', 
                   [])
    cls.add_method('Array', 
                   'ON_InstanceDefinition const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_InstanceDefinition *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_InstanceDefinition *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_InstanceDefinition *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_InstanceDefinition *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_InstanceDefinition &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_Layer_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_Layer > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Layer *', 
                   [])
    cls.add_method('First', 
                   'ON_Layer const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Layer *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Layer *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Layer *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Layer *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Layer const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Layer const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Layer const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Layer const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Layer *', 
                   [])
    cls.add_method('Last', 
                   'ON_Layer const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Layer &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Layer const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Layer const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Layer const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Layer const *', 'key'), param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Layer const *', 'key'), param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Layer const *', 'key'), param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Layer const *, ON_Layer const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Layer *', 
                   [param('ON_Layer *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Layer *', 
                   [])
    cls.add_method('Array', 
                   'ON_Layer const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Layer *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Layer *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Layer *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_Layer *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_Layer &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_Linetype_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_Linetype > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Linetype *', 
                   [])
    cls.add_method('First', 
                   'ON_Linetype const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Linetype *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Linetype *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Linetype *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Linetype *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Linetype const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Linetype const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Linetype const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Linetype const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Linetype *', 
                   [])
    cls.add_method('Last', 
                   'ON_Linetype const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Linetype &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Linetype const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Linetype const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Linetype const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Linetype const *', 'key'), param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Linetype const *', 'key'), param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Linetype const *', 'key'), param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Linetype const *, ON_Linetype const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Linetype *', 
                   [param('ON_Linetype *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Linetype *', 
                   [])
    cls.add_method('Array', 
                   'ON_Linetype const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Linetype *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Linetype *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Linetype *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_Linetype *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_Linetype &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_Localizer_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_Localizer > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Localizer *', 
                   [])
    cls.add_method('First', 
                   'ON_Localizer const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Localizer *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Localizer *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Localizer *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Localizer *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Localizer const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Localizer const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Localizer const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Localizer const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Localizer *', 
                   [])
    cls.add_method('Last', 
                   'ON_Localizer const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Localizer &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Localizer const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Localizer const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Localizer const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Localizer const *', 'key'), param('int ( * ) ( ON_Localizer const *, ON_Localizer const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Localizer const *', 'key'), param('int ( * ) ( ON_Localizer const *, ON_Localizer const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Localizer const *', 'key'), param('int ( * ) ( ON_Localizer const *, ON_Localizer const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Localizer const *, ON_Localizer const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Localizer const *, ON_Localizer const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Localizer const *, ON_Localizer const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Localizer const *, ON_Localizer const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Localizer *', 
                   [param('ON_Localizer *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Localizer *', 
                   [])
    cls.add_method('Array', 
                   'ON_Localizer const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Localizer *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Localizer *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Localizer *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_Localizer *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_Localizer &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_MappingRef_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_MappingRef > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MappingRef *', 
                   [])
    cls.add_method('First', 
                   'ON_MappingRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingRef *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MappingRef *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MappingRef *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MappingRef *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MappingRef const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingRef const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingRef const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingRef const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MappingRef *', 
                   [])
    cls.add_method('Last', 
                   'ON_MappingRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MappingRef &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MappingRef const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MappingRef const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MappingRef const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MappingRef const *', 'key'), param('int ( * ) ( ON_MappingRef const *, ON_MappingRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MappingRef const *', 'key'), param('int ( * ) ( ON_MappingRef const *, ON_MappingRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MappingRef const *', 'key'), param('int ( * ) ( ON_MappingRef const *, ON_MappingRef const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MappingRef const *, ON_MappingRef const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MappingRef const *, ON_MappingRef const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MappingRef const *, ON_MappingRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MappingRef const *, ON_MappingRef const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MappingRef *', 
                   [param('ON_MappingRef *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MappingRef *', 
                   [])
    cls.add_method('Array', 
                   'ON_MappingRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MappingRef *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MappingRef *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MappingRef *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_MappingRef *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_MappingRef &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_Material_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_Material > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Material *', 
                   [])
    cls.add_method('First', 
                   'ON_Material const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Material *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Material *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Material *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Material *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Material const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Material const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Material const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Material const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Material *', 
                   [])
    cls.add_method('Last', 
                   'ON_Material const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Material &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Material const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Material const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Material const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Material const *', 'key'), param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Material const *', 'key'), param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Material const *', 'key'), param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Material const *, ON_Material const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Material *', 
                   [param('ON_Material *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Material *', 
                   [])
    cls.add_method('Array', 
                   'ON_Material const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Material *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Material *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Material *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_Material *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_Material &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_MaterialRef_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_MaterialRef > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MaterialRef *', 
                   [])
    cls.add_method('First', 
                   'ON_MaterialRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MaterialRef *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MaterialRef *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MaterialRef *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MaterialRef *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MaterialRef const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MaterialRef const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MaterialRef const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MaterialRef const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MaterialRef *', 
                   [])
    cls.add_method('Last', 
                   'ON_MaterialRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MaterialRef &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MaterialRef const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MaterialRef const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MaterialRef const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MaterialRef const *', 'key'), param('int ( * ) ( ON_MaterialRef const *, ON_MaterialRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MaterialRef const *', 'key'), param('int ( * ) ( ON_MaterialRef const *, ON_MaterialRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MaterialRef const *', 'key'), param('int ( * ) ( ON_MaterialRef const *, ON_MaterialRef const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MaterialRef const *, ON_MaterialRef const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MaterialRef const *, ON_MaterialRef const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MaterialRef const *, ON_MaterialRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MaterialRef const *, ON_MaterialRef const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MaterialRef *', 
                   [param('ON_MaterialRef *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MaterialRef *', 
                   [])
    cls.add_method('Array', 
                   'ON_MaterialRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MaterialRef *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MaterialRef *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MaterialRef *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_MaterialRef *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_MaterialRef &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_PlugInRef_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_PlugInRef > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_PlugInRef *', 
                   [])
    cls.add_method('First', 
                   'ON_PlugInRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_PlugInRef *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_PlugInRef *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_PlugInRef *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_PlugInRef *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_PlugInRef const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_PlugInRef const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_PlugInRef const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_PlugInRef const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_PlugInRef *', 
                   [])
    cls.add_method('Last', 
                   'ON_PlugInRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_PlugInRef &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_PlugInRef const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_PlugInRef const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_PlugInRef const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_PlugInRef const *', 'key'), param('int ( * ) ( ON_PlugInRef const *, ON_PlugInRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_PlugInRef const *', 'key'), param('int ( * ) ( ON_PlugInRef const *, ON_PlugInRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_PlugInRef const *', 'key'), param('int ( * ) ( ON_PlugInRef const *, ON_PlugInRef const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_PlugInRef const *, ON_PlugInRef const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_PlugInRef const *, ON_PlugInRef const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_PlugInRef const *, ON_PlugInRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_PlugInRef const *, ON_PlugInRef const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_PlugInRef *', 
                   [param('ON_PlugInRef *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_PlugInRef *', 
                   [])
    cls.add_method('Array', 
                   'ON_PlugInRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_PlugInRef *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_PlugInRef *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_PlugInRef *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_PlugInRef *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_PlugInRef &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_Texture_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_Texture > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Texture *', 
                   [])
    cls.add_method('First', 
                   'ON_Texture const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Texture *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Texture *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Texture *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Texture *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Texture const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Texture const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Texture const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Texture const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Texture *', 
                   [])
    cls.add_method('Last', 
                   'ON_Texture const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Texture &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Texture const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Texture const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Texture const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Texture const *', 'key'), param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Texture const *', 'key'), param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Texture const *', 'key'), param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Texture const *, ON_Texture const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Texture *', 
                   [param('ON_Texture *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Texture *', 
                   [])
    cls.add_method('Array', 
                   'ON_Texture const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Texture *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Texture *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Texture *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_Texture *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_Texture &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_TextureCoordinates_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_TextureCoordinates > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_TextureCoordinates *', 
                   [])
    cls.add_method('First', 
                   'ON_TextureCoordinates const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureCoordinates *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_TextureCoordinates *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_TextureCoordinates *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_TextureCoordinates *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_TextureCoordinates const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureCoordinates const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureCoordinates const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureCoordinates const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_TextureCoordinates *', 
                   [])
    cls.add_method('Last', 
                   'ON_TextureCoordinates const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_TextureCoordinates &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_TextureCoordinates const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_TextureCoordinates const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_TextureCoordinates const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_TextureCoordinates const *', 'key'), param('int ( * ) ( ON_TextureCoordinates const *, ON_TextureCoordinates const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_TextureCoordinates const *', 'key'), param('int ( * ) ( ON_TextureCoordinates const *, ON_TextureCoordinates const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_TextureCoordinates const *', 'key'), param('int ( * ) ( ON_TextureCoordinates const *, ON_TextureCoordinates const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_TextureCoordinates const *, ON_TextureCoordinates const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_TextureCoordinates const *, ON_TextureCoordinates const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_TextureCoordinates const *, ON_TextureCoordinates const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_TextureCoordinates const *, ON_TextureCoordinates const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_TextureCoordinates *', 
                   [param('ON_TextureCoordinates *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_TextureCoordinates *', 
                   [])
    cls.add_method('Array', 
                   'ON_TextureCoordinates const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_TextureCoordinates *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_TextureCoordinates *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_TextureCoordinates *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_TextureCoordinates *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_TextureCoordinates &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_TextureMapping_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_TextureMapping > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_TextureMapping *', 
                   [])
    cls.add_method('First', 
                   'ON_TextureMapping const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureMapping *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_TextureMapping *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_TextureMapping *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_TextureMapping *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_TextureMapping const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureMapping const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureMapping const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_TextureMapping const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_TextureMapping *', 
                   [])
    cls.add_method('Last', 
                   'ON_TextureMapping const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_TextureMapping &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_TextureMapping const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_TextureMapping const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_TextureMapping const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_TextureMapping const *', 'key'), param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_TextureMapping const *', 'key'), param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_TextureMapping const *', 'key'), param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_TextureMapping *', 
                   [param('ON_TextureMapping *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_TextureMapping *', 
                   [])
    cls.add_method('Array', 
                   'ON_TextureMapping const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_TextureMapping *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_TextureMapping *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_TextureMapping *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_TextureMapping *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_TextureMapping &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassArray__ON_UserString_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ClassArray< ON_UserString > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_UserString *', 
                   [])
    cls.add_method('First', 
                   'ON_UserString const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UserString *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_UserString *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_UserString *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_UserString *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_UserString const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UserString const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UserString const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UserString const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_UserString *', 
                   [])
    cls.add_method('Last', 
                   'ON_UserString const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_UserString &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_UserString const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_UserString const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_UserString const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_UserString const *', 'key'), param('int ( * ) ( ON_UserString const *, ON_UserString const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UserString const *', 'key'), param('int ( * ) ( ON_UserString const *, ON_UserString const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UserString const *', 'key'), param('int ( * ) ( ON_UserString const *, ON_UserString const * ) *', 'compar'), param('int', 'count')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UserString const *, ON_UserString const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UserString const *, ON_UserString const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_UserString const *, ON_UserString const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_UserString const *, ON_UserString const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_UserString *', 
                   [param('ON_UserString *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_UserString *', 
                   [])
    cls.add_method('Array', 
                   'ON_UserString const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_UserString *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UserString *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UserString *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    cls.add_method('ConstructDefaultElement', 
                   'void', 
                   [param('ON_UserString *', 'p')], 
                   visibility='protected')
    cls.add_method('DestroyElement', 
                   'void', 
                   [param('ON_UserString &', 'x')], 
                   visibility='protected')
    return

def register_ON_ClassId_methods(root_module, cls):
    cls.add_constructor([param('char const *', 'sClassName'), param('char const *', 'sBaseClassName'), param('ON_Object * ( * ) (  ) *', 'create'), param('char const *', 'sUUID')])
    cls.add_constructor([param('char const *', 'sClassName'), param('char const *', 'sBaseClassName'), param('ON_Object * ( * ) (  ) *', 'create'), param('bool ( * ) ( ON_Object const *, ON_Object * ) *', 'copy'), param('char const *', 'sUUID')])
    cls.add_method('ClassId', 
                   'ON_ClassId const *', 
                   [param('char const *', 'sClassName')], 
                   is_static=True)
    cls.add_method('ClassId', 
                   'ON_ClassId const *', 
                   [param('ON_UUID', 'class_uuid')], 
                   is_static=True)
    cls.add_method('IncrementMark', 
                   'int', 
                   [], 
                   is_static=True)
    cls.add_method('CurrentMark', 
                   'int', 
                   [], 
                   is_static=True)
    cls.add_method('LastClassId', 
                   'ON_ClassId const *', 
                   [], 
                   is_static=True)
    cls.add_method('Purge', 
                   'int', 
                   [param('int', 'mark')], 
                   is_static=True)
    cls.add_method('PurgeAfter', 
                   'bool', 
                   [param('ON_ClassId const *', 'pClassId')], 
                   is_static=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'dump')], 
                   is_static=True)
    cls.add_method('ClassName', 
                   'char const *', 
                   [], 
                   is_const=True)
    cls.add_method('BaseClassName', 
                   'char const *', 
                   [], 
                   is_const=True)
    cls.add_method('BaseClass', 
                   'ON_ClassId const *', 
                   [], 
                   is_const=True)
    cls.add_method('IsDerivedFrom', 
                   'ON_BOOL32', 
                   [param('ON_ClassId const *', 'potential_parent')], 
                   is_const=True)
    cls.add_method('Create', 
                   'ON_Object *', 
                   [], 
                   is_const=True)
    cls.add_method('Uuid', 
                   'ON_UUID', 
                   [], 
                   is_const=True)
    cls.add_method('Mark', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('ClassIdVersion', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    return

def register_ON_ClippingPlane_methods(root_module, cls):
    cls.add_constructor([param('ON_ClippingPlane const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('ClippingPlaneInfo', 
                   'ON_ClippingPlaneInfo', 
                   [], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bEnabled', 'bool', is_const=False)
    cls.add_instance_attribute('m_plane', 'ON_Plane', is_const=False)
    cls.add_instance_attribute('m_plane_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_viewport_ids', 'ON_UuidList', is_const=False)
    return

def register_ON_ClippingPlaneInfo_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_ClippingPlaneInfo const &', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bEnabled', 'bool', is_const=False)
    cls.add_instance_attribute('m_plane_equation', 'ON_PlaneEquation', is_const=False)
    cls.add_instance_attribute('m_plane_id', 'ON_UUID', is_const=False)
    return

def register_ON_ClippingRegion_methods(root_module, cls):
    cls.add_constructor([param('ON_ClippingRegion const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('ClipPlaneTolerance', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('GetLineClipPlaneParamters', 
                   'bool', 
                   [param('ON_4dPoint', 'P0'), param('ON_4dPoint', 'P1'), param('double *', 't0'), param('double *', 't1')], 
                   is_const=True)
    cls.add_method('InClipPlaneRegion', 
                   'int', 
                   [param('ON_3dPoint', 'P')], 
                   is_const=True)
    cls.add_method('InClipPlaneRegion', 
                   'int', 
                   [param('ON_BoundingBox const &', 'bbox')], 
                   is_const=True)
    cls.add_method('InClipPlaneRegion', 
                   'int', 
                   [param('int', 'count'), param('ON_3fPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('InClipPlaneRegion', 
                   'int', 
                   [param('int', 'count'), param('ON_3dPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('InClipPlaneRegion', 
                   'int', 
                   [param('int', 'count'), param('ON_4dPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('InViewFrustum', 
                   'int', 
                   [param('ON_3dPoint', 'P')], 
                   is_const=True)
    cls.add_method('InViewFrustum', 
                   'int', 
                   [param('ON_BoundingBox const &', 'bbox')], 
                   is_const=True)
    cls.add_method('InViewFrustum', 
                   'int', 
                   [param('int', 'count'), param('ON_3fPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('InViewFrustum', 
                   'int', 
                   [param('int', 'count'), param('ON_3dPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('InViewFrustum', 
                   'int', 
                   [param('int', 'count'), param('ON_4dPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('IsVisible', 
                   'int', 
                   [param('ON_3dPoint', 'P')], 
                   is_const=True)
    cls.add_method('IsVisible', 
                   'int', 
                   [param('ON_BoundingBox const &', 'bbox')], 
                   is_const=True)
    cls.add_method('IsVisible', 
                   'int', 
                   [param('int', 'count'), param('ON_3fPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('IsVisible', 
                   'int', 
                   [param('int', 'count'), param('ON_3dPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('IsVisible', 
                   'int', 
                   [param('int', 'count'), param('ON_4dPoint const *', 'p')], 
                   is_const=True)
    cls.add_method('SetClipPlaneTolerance', 
                   'void', 
                   [param('double', 'clip_plane_tolerance')])
    cls.add_method('TransformPoint', 
                   'unsigned int', 
                   [param('ON_4dPoint const &', 'P'), param('ON_4dPoint &', 'Q')], 
                   is_const=True)
    cls.add_method('TransformPoint', 
                   'unsigned int', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dPoint &', 'Q')], 
                   is_const=True)
    cls.add_method('TransformPoint', 
                   'unsigned int', 
                   [param('ON_3fPoint const &', 'P'), param('ON_3dPoint &', 'Q')], 
                   is_const=True)
    cls.add_method('TransformPoints', 
                   'int', 
                   [param('int', 'count'), param('ON_4dPoint *', 'p')], 
                   is_const=True)
    cls.add_method('TransformPoints', 
                   'int', 
                   [param('int', 'count'), param('ON_4dPoint *', 'p'), param('unsigned int *', 'pflags')], 
                   is_const=True)
    cls.add_instance_attribute('m_clip_plane', 'ON_PlaneEquation [ 16 ]', is_const=False)
    cls.add_instance_attribute('m_clip_plane_count', 'int', is_const=False)
    cls.add_instance_attribute('m_xform', 'ON_Xform', is_const=False)
    return

def register_ON_Color_methods(root_module, cls):
    cls.add_constructor([param('ON_Color const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('int', 'red'), param('int', 'green'), param('int', 'blue')])
    cls.add_constructor([param('int', 'red'), param('int', 'green'), param('int', 'blue'), param('int', 'alpha')])
    cls.add_constructor([param('unsigned int', 'arg0')])
    cls.add_method('Alpha', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Blue', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_Color const &', 'arg0')], 
                   is_const=True)
    cls.add_method('FractionAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('FractionBlue', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('FractionGreen', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('FractionRed', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Green', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Hue', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Red', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Saturation', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('SetAlpha', 
                   'void', 
                   [param('int', 'alpha')])
    cls.add_method('SetFractionalAlpha', 
                   'void', 
                   [param('double', 'alpha')])
    cls.add_method('SetFractionalRGB', 
                   'void', 
                   [param('double', 'red'), param('double', 'green'), param('double', 'blue')])
    cls.add_method('SetFractionalRGBA', 
                   'void', 
                   [param('double', 'red'), param('double', 'green'), param('double', 'blue'), param('double', 'alpha')])
    cls.add_method('SetHSV', 
                   'void', 
                   [param('double', 'h'), param('double', 's'), param('double', 'v')])
    cls.add_method('SetRGB', 
                   'void', 
                   [param('int', 'red'), param('int', 'green'), param('int', 'blue')])
    cls.add_method('SetRGBA', 
                   'void', 
                   [param('int', 'red'), param('int', 'green'), param('int', 'blue'), param('int', 'alpha')])
    cls.add_method('Value', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('WindowsRGB', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_static_attribute('UnsetColor', 'ON_Color const', is_const=True)
    return

def register_ON_CompressStream_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_method('SetCallback', 
                   'bool', 
                   [param('ON_StreamCallbackFunction', 'callback_function'), param('void *', 'callback_context')])
    cls.add_method('CallbackFunction', 
                   'ON_StreamCallbackFunction', 
                   [], 
                   is_const=True)
    cls.add_method('CallbackContext', 
                   'void *', 
                   [], 
                   is_const=True)
    cls.add_method('Begin', 
                   'bool', 
                   [])
    cls.add_method('In', 
                   'bool', 
                   [param('ON__UINT64', 'in_buffer_size'), param('void const *', 'in_buffer')])
    cls.add_method('Out', 
                   'bool', 
                   [param('void *', 'callback_context'), param('ON__UINT32', 'out_buffer_size'), param('void const *', 'out_buffer')], 
                   is_virtual=True)
    cls.add_method('End', 
                   'bool', 
                   [])
    cls.add_method('InSize', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('OutSize', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('InCRC', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    cls.add_method('OutCRC', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    return

def register_ON_CompressedBuffer_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_CompressedBuffer const &', 'src')])
    cls.add_method('Compress', 
                   'bool', 
                   [param('size_t', 'sizeof__inbuffer'), param('void const *', 'inbuffer'), param('int', 'sizeof_element')])
    cls.add_method('CompressionEnd', 
                   'bool', 
                   [param('ON_CompressedBufferHelper *', 'arg0')], 
                   is_const=True)
    cls.add_method('CompressionInit', 
                   'bool', 
                   [param('ON_CompressedBufferHelper *', 'arg0')], 
                   is_const=True)
    cls.add_method('DeflateHelper', 
                   'size_t', 
                   [param('ON_CompressedBufferHelper *', 'arg0'), param('size_t', 'sizeof___inbuffer'), param('void const *', 'in___buffer')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('InflateHelper', 
                   'bool', 
                   [param('ON_CompressedBufferHelper *', 'arg0'), param('size_t', 'sizeof___outbuffer'), param('void *', 'out___buffer')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'binary_archive')])
    cls.add_method('SizeOfUncompressedBuffer', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('Uncompress', 
                   'bool', 
                   [param('void *', 'outbuffer'), param('int *', 'bFailedCRC')], 
                   is_const=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_const=True)
    cls.add_method('WriteChar', 
                   'bool', 
                   [param('size_t', 'count'), param('void const *', 'buffer')])
    cls.add_instance_attribute('m_buffer_compressed', 'void *', is_const=False)
    cls.add_instance_attribute('m_buffer_compressed_capacity', 'size_t', is_const=False)
    cls.add_instance_attribute('m_crc_compressed', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('m_crc_uncompressed', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('m_method', 'int', is_const=False)
    cls.add_instance_attribute('m_sizeof_compressed', 'size_t', is_const=False)
    cls.add_instance_attribute('m_sizeof_element', 'int', is_const=False)
    cls.add_instance_attribute('m_sizeof_uncompressed', 'size_t', is_const=False)
    return

def register_ON_Cone_methods(root_module, cls):
    cls.add_constructor([param('ON_Cone const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_Plane const &', 'plane'), param('double', 'height'), param('double', 'radius')])
    cls.add_method('AngleInDegrees', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('AngleInRadians', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('ApexPoint', 
                   'ON_3dPoint const &', 
                   [], 
                   is_const=True)
    cls.add_method('Axis', 
                   'ON_3dVector const &', 
                   [], 
                   is_const=True)
    cls.add_method('BasePoint', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('CircleAt', 
                   'ON_Circle', 
                   [param('double', 'height_parameter')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'bool', 
                   [param('ON_3dPoint', 'point'), param('double *', 'radial_parameter'), param('double *', 'height_parameter')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'arg0')], 
                   is_const=True)
    cls.add_method('Create', 
                   'ON_BOOL32', 
                   [param('ON_Plane const &', 'plane'), param('double', 'height'), param('double', 'radius')])
    cls.add_method('GetNurbForm', 
                   'ON_BOOL32', 
                   [param('ON_NurbsSurface &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True)
    cls.add_method('LineAt', 
                   'ON_Line', 
                   [param('double', 'radial_parameter')], 
                   is_const=True)
    cls.add_method('NormalAt', 
                   'ON_3dVector', 
                   [param('double', 'radial_parameter'), param('double', 'height_parameter')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'radial_parameter'), param('double', 'height_parameter')], 
                   is_const=True)
    cls.add_method('RevSurfaceForm', 
                   'ON_RevSurface *', 
                   [param('ON_RevSurface *', 'srf', default_value='0')], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'angle_in_radians'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'angle_in_radians'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Transform', 
                   'ON_BOOL32', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Translate', 
                   'ON_BOOL32', 
                   [param('ON_3dVector const &', 'delta')])
    cls.add_instance_attribute('height', 'double', is_const=False)
    cls.add_instance_attribute('plane', 'ON_Plane', is_const=False)
    cls.add_instance_attribute('radius', 'double', is_const=False)
    return

def register_ON_CurveProxyHistory_methods(root_module, cls):
    cls.add_constructor([param('ON_CurveProxyHistory const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_bReversed', 'bool', is_const=False)
    cls.add_instance_attribute('m_curve_ref', 'ON_ObjRef', is_const=False)
    cls.add_instance_attribute('m_full_real_curve_domain', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('m_proxy_curve_domain', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('m_sub_real_curve_domain', 'ON_Interval', is_const=False)
    return

def register_ON_Cylinder_methods(root_module, cls):
    cls.add_constructor([param('ON_Cylinder const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_Circle const &', 'arg0')])
    cls.add_constructor([param('ON_Circle const &', 'arg0'), param('double', 'arg1')])
    cls.add_method('Axis', 
                   'ON_3dVector const &', 
                   [], 
                   is_const=True)
    cls.add_method('Center', 
                   'ON_3dPoint const &', 
                   [], 
                   is_const=True)
    cls.add_method('CircleAt', 
                   'ON_Circle', 
                   [param('double', 'arg0')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'bool', 
                   [param('ON_3dPoint', 'arg0'), param('double *', 'arg1'), param('double *', 'arg2')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'arg0')], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_Circle const &', 'arg0')])
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_Circle const &', 'arg0'), param('double', 'arg1')])
    cls.add_method('GetNurbForm', 
                   'int', 
                   [param('ON_NurbsSurface &', 'arg0')], 
                   is_const=True)
    cls.add_method('Height', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('IsFinite', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('LineAt', 
                   'ON_Line', 
                   [param('double', 'arg0')], 
                   is_const=True)
    cls.add_method('NormalAt', 
                   'ON_3dPoint', 
                   [param('double', 'arg0'), param('double', 'arg1')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'arg0'), param('double', 'arg1')], 
                   is_const=True)
    cls.add_method('RevSurfaceForm', 
                   'ON_RevSurface *', 
                   [param('ON_RevSurface *', 'srf', default_value='0')], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'arg0'), param('double', 'arg1'), param('ON_3dVector const &', 'arg2')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'arg0'), param('ON_3dVector const &', 'arg1')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'arg0'), param('double', 'arg1'), param('ON_3dVector const &', 'arg2'), param('ON_3dPoint const &', 'arg3')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'arg0'), param('ON_3dVector const &', 'arg1'), param('ON_3dPoint const &', 'arg2')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_instance_attribute('circle', 'ON_Circle', is_const=False)
    cls.add_instance_attribute('height', 'double [ 2 ]', is_const=False)
    return

def register_ON_DecodeBase64_methods(root_module, cls):
    cls.add_constructor([param('ON_DecodeBase64 const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Begin', 
                   'void', 
                   [])
    cls.add_method('Decode', 
                   'char const *', 
                   [param('char const *', 'base64str')])
    cls.add_method('Decode', 
                   'char const *', 
                   [param('char const *', 'base64str'), param('size_t', 'base64str_count')])
    cls.add_method('Decode', 
                   'wchar_t const *', 
                   [param('wchar_t const *', 'base64str')])
    cls.add_method('Decode', 
                   'wchar_t const *', 
                   [param('wchar_t const *', 'base64str'), param('size_t', 'base64str_count')])
    cls.add_method('End', 
                   'bool', 
                   [])
    cls.add_method('Error', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Output', 
                   'void', 
                   [], 
                   is_virtual=True)
    cls.add_method('SetError', 
                   'void', 
                   [])
    cls.add_instance_attribute('m_decode_count', 'unsigned int', is_const=False)
    cls.add_instance_attribute('m_output', 'unsigned char [ 512 ]', is_const=False)
    cls.add_instance_attribute('m_output_count', 'int', is_const=False)
    return

def register_ON_DisplayMaterialRef_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>')
    cls.add_binary_comparison_operator('>=')
    cls.add_constructor([param('ON_DisplayMaterialRef const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_DisplayMaterialRef const &', 'other')], 
                   is_const=True)
    cls.add_instance_attribute('m_display_material_id', 'ON_UUID', is_const=False)
    cls.add_static_attribute('m_invisible_in_detail_id', 'ON_UUID const', is_const=True)
    cls.add_instance_attribute('m_viewport_id', 'ON_UUID', is_const=False)
    return

def register_ON_EarthAnchorPoint_methods(root_module, cls):
    cls.add_constructor([param('ON_EarthAnchorPoint const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_EarthAnchorPoint const *', 'arg0'), param('ON_EarthAnchorPoint const *', 'arg1')], 
                   is_static=True)
    cls.add_method('CompareEarthLocation', 
                   'int', 
                   [param('ON_EarthAnchorPoint const *', 'arg0'), param('ON_EarthAnchorPoint const *', 'arg1')], 
                   is_static=True)
    cls.add_method('CompareIdentification', 
                   'int', 
                   [param('ON_EarthAnchorPoint const *', 'arg0'), param('ON_EarthAnchorPoint const *', 'arg1')], 
                   is_static=True)
    cls.add_method('CompareModelDirection', 
                   'int', 
                   [param('ON_EarthAnchorPoint const *', 'arg0'), param('ON_EarthAnchorPoint const *', 'arg1')], 
                   is_static=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('GetModelCompass', 
                   'bool', 
                   [param('ON_Plane &', 'model_compass')], 
                   is_const=True)
    cls.add_method('GetModelToEarthXform', 
                   'bool', 
                   [param('ON_UnitSystem const &', 'model_unit_system'), param('ON_Xform &', 'model_to_earth')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_description', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_earth_basepoint_elevation', 'double', is_const=False)
    cls.add_instance_attribute('m_earth_basepoint_elevation_zero', 'int', is_const=False)
    cls.add_instance_attribute('m_earth_basepoint_latitude', 'double', is_const=False)
    cls.add_instance_attribute('m_earth_basepoint_longitude', 'double', is_const=False)
    cls.add_instance_attribute('m_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_model_basepoint', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_model_east', 'ON_3dVector', is_const=False)
    cls.add_instance_attribute('m_model_north', 'ON_3dVector', is_const=False)
    cls.add_instance_attribute('m_name', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_url', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_url_tag', 'ON_wString', is_const=False)
    return

def register_ON_Ellipse_methods(root_module, cls):
    cls.add_constructor([param('ON_Ellipse const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_Plane const &', 'arg0'), param('double', 'arg1'), param('double', 'arg2')])
    cls.add_constructor([param('ON_Circle const &', 'arg0')])
    cls.add_method('Center', 
                   'ON_3dPoint const &', 
                   [], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_BOOL32', 
                   [param('ON_3dPoint const &', 'arg0'), param('double *', 'arg1')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Create', 
                   'ON_BOOL32', 
                   [param('ON_Plane const &', 'arg0'), param('double', 'arg1'), param('double', 'arg2')])
    cls.add_method('Create', 
                   'ON_BOOL32', 
                   [param('ON_Circle const &', 'arg0')])
    cls.add_method('CurvatureAt', 
                   'ON_3dVector', 
                   [param('double', 'arg0')], 
                   is_const=True)
    cls.add_method('DerivativeAt', 
                   'ON_3dVector', 
                   [param('int', 'arg0'), param('double', 'arg1')], 
                   is_const=True)
    cls.add_method('EquationAt', 
                   'double', 
                   [param('ON_2dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('FocalDistance', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('GetFoci', 
                   'bool', 
                   [param('ON_3dPoint &', 'F1'), param('ON_3dPoint &', 'F2')], 
                   is_const=True)
    cls.add_method('GetNurbForm', 
                   'int', 
                   [param('ON_NurbsCurve &', 'arg0')], 
                   is_const=True)
    cls.add_method('GradientAt', 
                   'ON_2dVector', 
                   [param('ON_2dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsCircle', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True)
    cls.add_method('Normal', 
                   'ON_3dVector const &', 
                   [], 
                   is_const=True)
    cls.add_method('Plane', 
                   'ON_Plane const &', 
                   [], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'arg0')], 
                   is_const=True)
    cls.add_method('Radius', 
                   'double', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'arg0'), param('double', 'arg1'), param('ON_3dVector const &', 'arg2')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'arg0'), param('ON_3dVector const &', 'arg1')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'arg0'), param('double', 'arg1'), param('ON_3dVector const &', 'arg2'), param('ON_3dPoint const &', 'arg3')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'arg0'), param('ON_3dVector const &', 'arg1'), param('ON_3dPoint const &', 'arg2')])
    cls.add_method('TangentAt', 
                   'ON_3dVector', 
                   [param('double', 'arg0')], 
                   is_const=True)
    cls.add_method('Translate', 
                   'ON_BOOL32', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_instance_attribute('plane', 'ON_Plane', is_const=False)
    cls.add_instance_attribute('radius', 'double [ 2 ]', is_const=False)
    return

def register_ON_Evaluator_methods(root_module, cls):
    cls.add_instance_attribute('m_parameter_count', 'int const', is_const=True)
    cls.add_instance_attribute('m_value_count', 'int const', is_const=True)
    cls.add_instance_attribute('m_domain', 'ON_SimpleArray< ON_Interval >', is_const=False)
    cls.add_instance_attribute('m_bPeriodicParameter', 'ON_SimpleArray< bool >', is_const=False)
    cls.add_constructor([param('ON_Evaluator const &', 'arg0')])
    cls.add_constructor([param('int', 'parameter_count'), param('int', 'value_count'), param('ON_Interval const *', 'domain'), param('bool const *', 'periodic')])
    cls.add_method('Evaluate', 
                   'int', 
                   [param('double const *', 'parameters'), param('double *', 'values'), param('double * *', 'jacobian')], 
                   is_pure_virtual=True, is_virtual=True)
    cls.add_method('EvaluateHessian', 
                   'int', 
                   [param('double const *', 'parameters'), param('double *', 'value'), param('double *', 'gradient'), param('double * *', 'hessian')], 
                   is_virtual=True)
    cls.add_method('FiniteDomain', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Periodic', 
                   'bool', 
                   [param('int', 'parameter_index')], 
                   is_const=True)
    cls.add_method('Domain', 
                   'ON_Interval', 
                   [param('int', 'parameter_index')], 
                   is_const=True)
    return

def register_ON_FileIterator_methods(root_module, cls):
    cls.add_constructor([param('ON_FileIterator const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Count', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentFileCreateTime', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentFileIsDirectory', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentFileIsHidden', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentFileLastAccessTime', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentFileLastModifiedTime', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentFileName', 
                   'wchar_t const *', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentFileSize', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('FirstFile', 
                   'wchar_t const *', 
                   [param('wchar_t const *', 'directory_name'), param('wchar_t const *', 'file_name_filter')])
    cls.add_method('FirstFile', 
                   'wchar_t const *', 
                   [param('char const *', 'directory_name'), param('char const *', 'file_name_filter')])
    cls.add_method('GetCurrentFullPathFileName', 
                   'bool', 
                   [param('ON_wString &', 'filename')], 
                   is_const=True)
    cls.add_method('NextFile', 
                   'wchar_t const *', 
                   [])
    return

def register_ON_FileStream_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_FileStream const &', 'arg0')])
    cls.add_method('Close', 
                   'int', 
                   [param('FILE *', 'fp')], 
                   is_static=True)
    cls.add_method('CurrentPosition', 
                   'ON__INT64', 
                   [param('FILE *', 'fp')], 
                   is_static=True)
    cls.add_method('Flush', 
                   'bool', 
                   [param('FILE *', 'fp')], 
                   is_static=True)
    cls.add_method('GetFileInformation', 
                   'bool', 
                   [param('FILE *', 'fp'), param('ON__UINT64 *', 'file_size'), param('ON__UINT64 *', 'file_create_time'), param('ON__UINT64 *', 'file_last_modified_time')], 
                   is_static=True)
    cls.add_method('Open', 
                   'FILE *', 
                   [param('wchar_t const *', 'filename'), param('wchar_t const *', 'mode')], 
                   is_static=True)
    cls.add_method('Open', 
                   'FILE *', 
                   [param('char const *', 'filename'), param('char const *', 'mode')], 
                   is_static=True)
    cls.add_method('Read', 
                   'ON__UINT64', 
                   [param('FILE *', 'fp'), param('ON__UINT64', 'count'), param('void *', 'buffer')], 
                   is_static=True)
    cls.add_method('Seek', 
                   'bool', 
                   [param('FILE *', 'fp'), param('ON__INT64', 'offset'), param('int', 'orgin')], 
                   is_static=True)
    cls.add_method('SeekFromCurrentPosition', 
                   'bool', 
                   [param('FILE *', 'fp'), param('ON__INT64', 'offset')], 
                   is_static=True)
    cls.add_method('SeekFromEnd', 
                   'bool', 
                   [param('FILE *', 'fp'), param('ON__INT64', 'offset')], 
                   is_static=True)
    cls.add_method('SeekFromStart', 
                   'bool', 
                   [param('FILE *', 'fp'), param('ON__INT64', 'offset')], 
                   is_static=True)
    cls.add_method('Write', 
                   'ON__UINT64', 
                   [param('FILE *', 'fp'), param('ON__UINT64', 'count'), param('void const *', 'buffer')], 
                   is_static=True)
    return

def register_ON_FixedSizePool_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_method('Create', 
                   'bool', 
                   [param('size_t', 'sizeof_element'), param('size_t', 'element_count_estimate'), param('size_t', 'block_element_capacity')])
    cls.add_method('SizeofElement', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('AllocateElement', 
                   'void *', 
                   [])
    cls.add_method('ReturnElement', 
                   'void', 
                   [param('void *', 'p')])
    cls.add_method('ReturnAll', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('ActiveElementCount', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('TotalElementCount', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('FirstElement', 
                   'void *', 
                   [])
    cls.add_method('FirstElement', 
                   'void *', 
                   [param('size_t', 'element_index')])
    cls.add_method('NextElement', 
                   'void *', 
                   [])
    cls.add_method('FirstBlock', 
                   'void *', 
                   [param('size_t *', 'block_element_count')])
    cls.add_method('NextBlock', 
                   'void *', 
                   [param('size_t *', 'block_element_count')])
    cls.add_method('Element', 
                   'void *', 
                   [param('size_t', 'element_index')], 
                   is_const=True)
    cls.add_method('SetHeap', 
                   'void', 
                   [param('void *', 'heap')])
    cls.add_method('Heap', 
                   'void *', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    return

def register_ON_FixedSizePoolIterator_methods(root_module, cls):
    cls.add_instance_attribute('m_fsp', 'ON_FixedSizePool const &', is_const=False)
    cls.add_constructor([param('ON_FixedSizePoolIterator const &', 'arg0')])
    cls.add_constructor([param('ON_FixedSizePool const &', 'fsp')])
    cls.add_method('FirstElement', 
                   'void *', 
                   [])
    cls.add_method('FirstElement', 
                   'void *', 
                   [param('size_t', 'element_index')])
    cls.add_method('NextElement', 
                   'void *', 
                   [])
    cls.add_method('FirstBlock', 
                   'void *', 
                   [param('size_t *', 'block_element_count')])
    cls.add_method('NextBlock', 
                   'void *', 
                   [param('size_t *', 'block_element_count')])
    return

def register_ON_HatchLine_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_HatchLine const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 'angle'), param('ON_2dPoint const &', 'base'), param('ON_2dVector const &', 'offset'), param('ON_SimpleArray< double > const', 'dashes')])
    cls.add_method('Angle', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('AppendDash', 
                   'void', 
                   [param('double', 'dash')])
    cls.add_method('Base', 
                   'ON_2dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('Dash', 
                   'double', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('DashCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('GetLineData', 
                   'void', 
                   [param('double &', 'angle'), param('ON_2dPoint &', 'base'), param('ON_2dVector &', 'offset'), param('ON_SimpleArray< double > &', 'dashes')], 
                   is_const=True)
    cls.add_method('GetPatternLength', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True)
    cls.add_method('Offset', 
                   'ON_2dVector', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('SetAngle', 
                   'void', 
                   [param('double', 'angle')])
    cls.add_method('SetBase', 
                   'void', 
                   [param('ON_2dPoint const &', 'base')])
    cls.add_method('SetOffset', 
                   'void', 
                   [param('ON_2dVector const &', 'offset')])
    cls.add_method('SetPattern', 
                   'void', 
                   [param('ON_SimpleArray< double > const &', 'dashes')])
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_angle', 'double', is_const=False)
    cls.add_instance_attribute('m_base', 'ON_2dPoint', is_const=False)
    cls.add_instance_attribute('m_dashes', 'ON_SimpleArray< double >', is_const=False)
    cls.add_instance_attribute('m_offset', 'ON_2dVector', is_const=False)
    return

def register_ON_HatchLoop_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_Curve *', 'pCurve2d'), param('ON_HatchLoop::eLoopType', 'type', default_value='::ON_HatchLoop::ltOuter')])
    cls.add_constructor([param('ON_HatchLoop const &', 'src')])
    cls.add_method('Curve', 
                   'ON_Curve const *', 
                   [], 
                   is_const=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('SetCurve', 
                   'bool', 
                   [param('ON_Curve const &', 'curve')])
    cls.add_method('SetType', 
                   'void', 
                   [param('ON_HatchLoop::eLoopType', 'type')])
    cls.add_method('Type', 
                   'ON_HatchLoop::eLoopType', 
                   [], 
                   is_const=True)
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    return

def register_ON_Interval_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('==')
    cls.add_constructor([param('ON_Interval const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 't0'), param('double', 't1')])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_Interval const &', 'other')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Includes', 
                   'bool', 
                   [param('double', 't'), param('bool', 'bTestOpenInterval', default_value='false')], 
                   is_const=True)
    cls.add_method('Includes', 
                   'bool', 
                   [param('ON_Interval const &', 'other'), param('bool', 'bProperSubSet', default_value='false')], 
                   is_const=True)
    cls.add_method('Intersection', 
                   'bool', 
                   [param('ON_Interval const &', 'arg0')])
    cls.add_method('Intersection', 
                   'bool', 
                   [param('ON_Interval const &', 'arg0'), param('ON_Interval const &', 'arg1')])
    cls.add_method('IsDecreasing', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsEmptyInterval', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsEmptySet', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsIncreasing', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsInterval', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsSingleton', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Length', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MakeIncreasing', 
                   'bool', 
                   [])
    cls.add_method('Max', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Mid', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Min', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('NormalizedParameterAt', 
                   'double', 
                   [param('double', 'interval_parameter')], 
                   is_const=True)
    cls.add_method('NormalizedParameterAt', 
                   'ON_Interval', 
                   [param('ON_Interval', 'interval_parameter')], 
                   is_const=True)
    cls.add_method('ParameterAt', 
                   'double', 
                   [param('double', 'normalized_parameter')], 
                   is_const=True)
    cls.add_method('ParameterAt', 
                   'ON_Interval', 
                   [param('ON_Interval', 'normalized_interval')], 
                   is_const=True)
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Set', 
                   'void', 
                   [param('double', 't0'), param('double', 't1')])
    cls.add_method('Swap', 
                   'void', 
                   [])
    cls.add_method('Union', 
                   'bool', 
                   [param('ON_Interval const &', 'arg0')])
    cls.add_method('Union', 
                   'bool', 
                   [param('double', 't')])
    cls.add_method('Union', 
                   'bool', 
                   [param('int', 'count'), param('double const *', 't')])
    cls.add_method('Union', 
                   'bool', 
                   [param('ON_Interval const &', 'arg0'), param('ON_Interval const &', 'arg1')])
    cls.add_static_attribute('EmptyInterval', 'ON_Interval const', is_const=True)
    cls.add_instance_attribute('m_t', 'double [ 2 ]', is_const=False)
    return

def register_ON_Line_methods(root_module, cls):
    cls.add_constructor([param('ON_Line const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dPoint const &', 'start'), param('ON_3dPoint const &', 'end')])
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'bool', 
                   [param('ON_3dPoint const &', 'test_point'), param('double *', 't')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint const &', 'test_point')], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_3dPoint const &', 'start'), param('ON_3dPoint const &', 'end')])
    cls.add_method('Direction', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('DistanceTo', 
                   'double', 
                   [param('ON_3dPoint', 'test_point')], 
                   is_const=True)
    cls.add_method('GetBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox &', 'bbox'), param('int', 'bGrowBox', default_value='false')], 
                   is_const=True)
    cls.add_method('GetTightBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox &', 'tight_bbox'), param('int', 'bGrowBox', default_value='false'), param('ON_Xform const *', 'xform', default_value='0')], 
                   is_const=True)
    cls.add_method('InPlane', 
                   'bool', 
                   [param('ON_Plane &', 'plane'), param('double', 'tolerance', default_value='0.0')], 
                   is_const=True)
    cls.add_method('IntersectSurface', 
                   'int', 
                   [param('ON_Surface const *', 'surfaceB'), param('ON_SimpleArray< ON_X_EVENT > &', 'x'), param('double', 'intersection_tolerance', default_value='0.0'), param('double', 'overlap_tolerance', default_value='0.0'), param('ON_Interval const *', 'line_domain', default_value='0'), param('ON_Interval const *', 'surfaceB_udomain', default_value='0'), param('ON_Interval const *', 'surfaceB_vdomain', default_value='0')], 
                   is_const=True)
    cls.add_method('IsFartherThan', 
                   'bool', 
                   [param('double', 'd'), param('ON_3dPoint const &', 'P')], 
                   is_const=True)
    cls.add_method('IsFartherThan', 
                   'bool', 
                   [param('double', 'd'), param('ON_Line const &', 'L')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Length', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumDistanceTo', 
                   'double', 
                   [param('ON_3dPoint const &', 'P')], 
                   is_const=True)
    cls.add_method('MaximumDistanceTo', 
                   'double', 
                   [param('ON_Line const &', 'other')], 
                   is_const=True)
    cls.add_method('MinimumDistanceTo', 
                   'double', 
                   [param('ON_3dPoint const &', 'P')], 
                   is_const=True)
    cls.add_method('MinimumDistanceTo', 
                   'double', 
                   [param('ON_Line const &', 'L')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 't')], 
                   is_const=True)
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle_in_radians'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Tangent', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'delta')])
    cls.add_instance_attribute('from', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('to', 'ON_3dPoint', is_const=False)
    return

def register_ON_LinetypeSegment_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_LinetypeSegment const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_length', 'double', is_const=False)
    cls.add_instance_attribute('m_seg_type', 'ON_LinetypeSegment::eSegType', is_const=False)
    return

def register_ON_LocalZero1_methods(root_module, cls):
    cls.add_constructor([param('ON_LocalZero1 const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Evaluate', 
                   'ON_BOOL32', 
                   [param('double', 'arg0'), param('double *', 'arg1'), param('double *', 'arg2'), param('int', 'arg3')], 
                   is_pure_virtual=True, is_virtual=True)
    cls.add_method('FindZero', 
                   'ON_BOOL32', 
                   [param('double *', 'arg0')])
    cls.add_instance_attribute('m_f_tolerance', 'double', is_const=False)
    cls.add_instance_attribute('m_k', 'double const *', is_const=False)
    cls.add_instance_attribute('m_k_count', 'int', is_const=False)
    cls.add_instance_attribute('m_t0', 'double', is_const=False)
    cls.add_instance_attribute('m_t1', 'double', is_const=False)
    cls.add_instance_attribute('m_t_tolerance', 'double', is_const=False)
    return

def register_ON_Localizer_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_Localizer const &', 'arg0')])
    cls.add_method('CreateCylinderLocalizer', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('ON_3dVector', 'D'), param('double', 'r0'), param('double', 'r1')])
    cls.add_method('CreatePlaneLocalizer', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('ON_3dVector', 'N'), param('double', 'h0'), param('double', 'h1')])
    cls.add_method('CreateSphereLocalizer', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('double', 'r0'), param('double', 'r1')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('IsZero', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'bbox')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Value', 
                   'double', 
                   [param('ON_3dPoint', 'P')], 
                   is_const=True)
    cls.add_method('Value', 
                   'double', 
                   [param('double', 'distance')], 
                   is_const=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_P', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_V', 'ON_3dVector', is_const=False)
    cls.add_instance_attribute('m_d', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('m_nurbs_curve', 'ON_NurbsCurve *', is_const=False)
    cls.add_instance_attribute('m_nurbs_surface', 'ON_NurbsSurface *', is_const=False)
    cls.add_instance_attribute('m_type', 'ON_Localizer::TYPE', is_const=False)
    return

def register_ON_MappingChannel_methods(root_module, cls):
    cls.add_constructor([param('ON_MappingChannel const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_MappingChannel const &', 'other')], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')], 
                   is_const=True)
    cls.add_instance_attribute('m_mapping_channel_id', 'int', is_const=False)
    cls.add_instance_attribute('m_mapping_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_mapping_index', 'int', is_const=False)
    cls.add_instance_attribute('m_object_xform', 'ON_Xform', is_const=False)
    return

def register_ON_MappingRef_methods(root_module, cls):
    cls.add_constructor([param('ON_MappingRef const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('AddMappingChannel', 
                   'bool', 
                   [param('int', 'mapping_channel_id'), param('ON_UUID const &', 'mapping_id')])
    cls.add_method('ChangeMappingChannel', 
                   'bool', 
                   [param('int', 'old_mapping_channel_id'), param('int', 'new_mapping_channel_id')])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_MappingRef const &', 'other')], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('DeleteMappingChannel', 
                   'bool', 
                   [param('int', 'mapping_channel_id')])
    cls.add_method('DeleteMappingChannel', 
                   'bool', 
                   [param('ON_UUID const &', 'mapping_id')])
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'text_log')], 
                   is_const=True)
    cls.add_method('MappingChannel', 
                   'ON_MappingChannel const *', 
                   [param('int', 'mapping_channel_id')], 
                   is_const=True)
    cls.add_method('MappingChannel', 
                   'ON_MappingChannel const *', 
                   [param('ON_UUID const &', 'mapping_id')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')])
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')], 
                   is_const=True)
    cls.add_instance_attribute('m_mapping_channels', 'ON_SimpleArray< ON_MappingChannel >', is_const=False)
    cls.add_instance_attribute('m_plugin_id', 'ON_UUID', is_const=False)
    return

def register_ON_MappingTag_methods(root_module, cls):
    cls.add_constructor([param('ON_MappingTag const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_MappingTag const &', 'other'), param('bool', 'bCompareId', default_value='true'), param('bool', 'bCompareCRC', default_value='true'), param('bool', 'bCompareXform', default_value='true')], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsDefaultSurfaceParameterMapping', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsSet', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Set', 
                   'void', 
                   [param('ON_TextureMapping const &', 'mapping')])
    cls.add_method('SetDefaultSurfaceParameterMappingTag', 
                   'void', 
                   [])
    cls.add_method('Transform', 
                   'void', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_mapping_crc', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('m_mapping_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_mapping_type', 'ON_TextureMapping::TYPE', is_const=False)
    cls.add_instance_attribute('m_mesh_xform', 'ON_Xform', is_const=False)
    return

def register_ON_MassProperties_methods(root_module, cls):
    cls.add_constructor([param('ON_MassProperties const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Area', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Centroid', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('CentroidCoordIntertiaMatrix', 
                   'ON_Matrix *', 
                   [param('ON_Matrix *', 'matrix', default_value='0')], 
                   is_const=True)
    cls.add_method('CentroidCoordMomentsOfInertia', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('CentroidCoordPrincipalMoments', 
                   'bool', 
                   [param('double *', 'pxx'), param('ON_3dVector &', 'Ax'), param('double *', 'pyy'), param('ON_3dVector &', 'Ay'), param('double *', 'pzz'), param('ON_3dVector &', 'Az')], 
                   is_const=True)
    cls.add_method('CentroidCoordRadiiOfGyration', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('CentroidCoordSecondMoments', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('Create', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'dump')], 
                   is_const=True)
    cls.add_method('Length', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('Sum', 
                   'bool', 
                   [param('int', 'count'), param('ON_MassProperties const *', 'summands'), param('bool', 'bAddTo', default_value='false')])
    cls.add_method('Volume', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('WorldCoordFirstMoments', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('WorldCoordIntertiaMatrix', 
                   'ON_Matrix *', 
                   [param('ON_Matrix *', 'matrix', default_value='0')], 
                   is_const=True)
    cls.add_method('WorldCoordMomentsOfInertia', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('WorldCoordPrincipalMoments', 
                   'bool', 
                   [param('double *', 'pxx'), param('ON_3dVector &', 'Ax'), param('double *', 'pyy'), param('ON_3dVector &', 'Ay'), param('double *', 'pzz'), param('ON_3dVector &', 'Az')], 
                   is_const=True)
    cls.add_method('WorldCoordRadiiOfGyration', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('WorldCoordSecondMoments', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_instance_attribute('m__bReserved1', 'bool', is_const=False)
    cls.add_instance_attribute('m__bReserved2', 'bool', is_const=False)
    cls.add_instance_attribute('m__bReserved3', 'bool', is_const=False)
    cls.add_instance_attribute('m__reserved', 'int', is_const=False)
    cls.add_instance_attribute('m__reserved1', 'double', is_const=False)
    cls.add_instance_attribute('m__reserved2', 'double', is_const=False)
    cls.add_instance_attribute('m__reserved3', 'double', is_const=False)
    cls.add_instance_attribute('m__reserved4', 'double', is_const=False)
    cls.add_instance_attribute('m__reserved5', 'double', is_const=False)
    cls.add_instance_attribute('m__reserved6', 'double', is_const=False)
    cls.add_instance_attribute('m__reserved7', 'double', is_const=False)
    cls.add_instance_attribute('m__reserved8', 'double', is_const=False)
    cls.add_instance_attribute('m_bValidCentroid', 'bool', is_const=False)
    cls.add_instance_attribute('m_bValidFirstMoments', 'bool', is_const=False)
    cls.add_instance_attribute('m_bValidMass', 'bool', is_const=False)
    cls.add_instance_attribute('m_bValidProductMoments', 'bool', is_const=False)
    cls.add_instance_attribute('m_bValidSecondMoments', 'bool', is_const=False)
    cls.add_instance_attribute('m_ccs_xx', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_xx_err', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_xy', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_xy_err', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_yy', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_yy_err', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_yz', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_yz_err', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_zx', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_zx_err', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_zz', 'double', is_const=False)
    cls.add_instance_attribute('m_ccs_zz_err', 'double', is_const=False)
    cls.add_instance_attribute('m_mass', 'double', is_const=False)
    cls.add_instance_attribute('m_mass_err', 'double', is_const=False)
    cls.add_instance_attribute('m_mass_type', 'int', is_const=False)
    cls.add_instance_attribute('m_world_x', 'double', is_const=False)
    cls.add_instance_attribute('m_world_x_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_xx', 'double', is_const=False)
    cls.add_instance_attribute('m_world_xx_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_xy', 'double', is_const=False)
    cls.add_instance_attribute('m_world_xy_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_y', 'double', is_const=False)
    cls.add_instance_attribute('m_world_y_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_yy', 'double', is_const=False)
    cls.add_instance_attribute('m_world_yy_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_yz', 'double', is_const=False)
    cls.add_instance_attribute('m_world_yz_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_z', 'double', is_const=False)
    cls.add_instance_attribute('m_world_z_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_zx', 'double', is_const=False)
    cls.add_instance_attribute('m_world_zx_err', 'double', is_const=False)
    cls.add_instance_attribute('m_world_zz', 'double', is_const=False)
    cls.add_instance_attribute('m_world_zz_err', 'double', is_const=False)
    cls.add_instance_attribute('m_x0', 'double', is_const=False)
    cls.add_instance_attribute('m_x0_err', 'double', is_const=False)
    cls.add_instance_attribute('m_y0', 'double', is_const=False)
    cls.add_instance_attribute('m_y0_err', 'double', is_const=False)
    cls.add_instance_attribute('m_z0', 'double', is_const=False)
    cls.add_instance_attribute('m_z0_err', 'double', is_const=False)
    return

def register_ON_MaterialRef_methods(root_module, cls):
    cls.add_constructor([param('ON_MaterialRef const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_MaterialRef const &', 'other')], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('MaterialSource', 
                   'ON::object_material_source', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')], 
                   is_const=True)
    cls.add_instance_attribute('m_material_backface_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_material_backface_index', 'int', is_const=False)
    cls.add_instance_attribute('m_material_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_material_index', 'int', is_const=False)
    cls.add_instance_attribute('m_material_source', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_plugin_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_reserved1', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_reserved2', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_reserved3', 'unsigned char', is_const=False)
    return

def register_ON_Matrix_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'row_count'), param('int', 'col_count')])
    cls.add_constructor([param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2'), param('int', 'arg3')])
    cls.add_constructor([param('ON_Xform const &', 'arg0')])
    cls.add_constructor([param('ON_Matrix const &', 'arg0')])
    cls.add_constructor([param('int', 'row_count'), param('int', 'col_count'), param('double * *', 'M'), param('bool', 'bDestructorFreeM')])
    cls.add_method('Add', 
                   'bool', 
                   [param('ON_Matrix const &', 'A'), param('ON_Matrix const &', 'B')])
    cls.add_method('BackSolve', 
                   'bool', 
                   [param('double', 'arg0'), param('int', 'arg1'), param('double const *', 'arg2'), param('double *', 'arg3')], 
                   is_const=True)
    cls.add_method('BackSolve', 
                   'bool', 
                   [param('double', 'arg0'), param('int', 'arg1'), param('ON_3dPoint const *', 'arg2'), param('ON_3dPoint *', 'arg3')], 
                   is_const=True)
    cls.add_method('BackSolve', 
                   'bool', 
                   [param('double', 'arg0'), param('int', 'arg1'), param('int', 'arg2'), param('int', 'arg3'), param('double const *', 'arg4'), param('int', 'arg5'), param('double *', 'arg6')], 
                   is_const=True)
    cls.add_method('ColCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('ColOp', 
                   'void', 
                   [param('int', 'arg0'), param('double', 'arg1'), param('int', 'arg2')])
    cls.add_method('ColScale', 
                   'void', 
                   [param('int', 'arg0'), param('double', 'arg1')])
    cls.add_method('Create', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('Create', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2'), param('int', 'arg3')])
    cls.add_method('Create', 
                   'bool', 
                   [param('int', 'row_count'), param('int', 'col_count'), param('double * *', 'M'), param('bool', 'bDestructorFreeM')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Invert', 
                   'bool', 
                   [param('double', 'arg0')])
    cls.add_method('IsColOrthoNormal', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsColOrthoganal', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsRowOrthoNormal', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsRowOrthoganal', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsSquare', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('MaxCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('MinCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Multiply', 
                   'bool', 
                   [param('ON_Matrix const &', 'A'), param('ON_Matrix const &', 'B')])
    cls.add_method('RowCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('RowOp', 
                   'void', 
                   [param('int', 'arg0'), param('double', 'arg1'), param('int', 'arg2')])
    cls.add_method('RowReduce', 
                   'int', 
                   [param('double', 'arg0'), param('double &', 'arg1'), param('double &', 'arg2')])
    cls.add_method('RowReduce', 
                   'int', 
                   [param('double', 'arg0'), param('double *', 'arg1'), param('double *', 'arg2', default_value='0')])
    cls.add_method('RowReduce', 
                   'int', 
                   [param('double', 'arg0'), param('ON_3dPoint *', 'arg1'), param('double *', 'arg2', default_value='0')])
    cls.add_method('RowReduce', 
                   'int', 
                   [param('double', 'arg0'), param('int', 'arg1'), param('int', 'arg2'), param('double *', 'arg3'), param('double *', 'arg4', default_value='0')])
    cls.add_method('RowScale', 
                   'void', 
                   [param('int', 'arg0'), param('double', 'arg1')])
    cls.add_method('Scale', 
                   'bool', 
                   [param('double', 's')])
    cls.add_method('SetDiagonal', 
                   'void', 
                   [param('double', 'arg0')])
    cls.add_method('SetDiagonal', 
                   'void', 
                   [param('double const *', 'arg0')])
    cls.add_method('SetDiagonal', 
                   'void', 
                   [param('int', 'arg0'), param('double const *', 'arg1')])
    cls.add_method('SetDiagonal', 
                   'void', 
                   [param('ON_SimpleArray< double > const &', 'arg0')])
    cls.add_method('SwapCols', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('SwapRows', 
                   'bool', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('Transpose', 
                   'bool', 
                   [])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_instance_attribute('m', 'double * *', is_const=False)
    return

def register_ON_MeshCurvatureStats_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshCurvatureStats const &', 'arg0')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Set', 
                   'bool', 
                   [param('ON::curvature_style', 'arg0'), param('int', 'arg1'), param('ON_SurfaceCurvature const *', 'arg2'), param('ON_3fVector const *', 'arg3'), param('double', 'arg4', default_value='0.0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_adev', 'double', is_const=False)
    cls.add_instance_attribute('m_average', 'double', is_const=False)
    cls.add_instance_attribute('m_count', 'int', is_const=False)
    cls.add_instance_attribute('m_count_infinite', 'int', is_const=False)
    cls.add_instance_attribute('m_infinity', 'double', is_const=False)
    cls.add_instance_attribute('m_mode', 'double', is_const=False)
    cls.add_instance_attribute('m_range', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('m_style', 'ON::curvature_style', is_const=False)
    return

def register_ON_MeshCurveParameters_methods(root_module, cls):
    cls.add_constructor([param('ON_MeshCurveParameters const &', 'arg0')])
    cls.add_constructor([])
    cls.add_instance_attribute('m_main_seg_count', 'int', is_const=False)
    cls.add_instance_attribute('m_max_ang_radians', 'double', is_const=False)
    cls.add_instance_attribute('m_max_aspect', 'double', is_const=False)
    cls.add_instance_attribute('m_max_chr', 'double', is_const=False)
    cls.add_instance_attribute('m_max_edge_length', 'double', is_const=False)
    cls.add_instance_attribute('m_min_edge_length', 'double', is_const=False)
    cls.add_instance_attribute('m_reserved1', 'int', is_const=False)
    cls.add_instance_attribute('m_reserved2', 'int', is_const=False)
    cls.add_instance_attribute('m_reserved3', 'double', is_const=False)
    cls.add_instance_attribute('m_reserved4', 'double', is_const=False)
    cls.add_instance_attribute('m_sub_seg_count', 'int', is_const=False)
    cls.add_instance_attribute('m_tolerance', 'double', is_const=False)
    return

def register_ON_MeshFace_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshFace const &', 'arg0')])
    cls.add_method('ComputeFaceNormal', 
                   'bool', 
                   [param('ON_3dPoint const *', 'dV'), param('ON_3dVector &', 'FN')], 
                   is_const=True)
    cls.add_method('ComputeFaceNormal', 
                   'bool', 
                   [param('ON_3fPoint const *', 'fV'), param('ON_3dVector &', 'FN')], 
                   is_const=True)
    cls.add_method('Flip', 
                   'void', 
                   [])
    cls.add_method('IsQuad', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsTriangle', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('int', 'mesh_vertex_count')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('int', 'mesh_vertex_count'), param('ON_3fPoint const *', 'V')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('int', 'mesh_vertex_count'), param('ON_3dPoint const *', 'V')], 
                   is_const=True)
    cls.add_method('Repair', 
                   'bool', 
                   [param('int', 'mesh_vertex_count')])
    cls.add_method('Repair', 
                   'bool', 
                   [param('int', 'mesh_vertex_count'), param('ON_3fPoint const *', 'V')])
    cls.add_method('Repair', 
                   'bool', 
                   [param('int', 'mesh_vertex_count'), param('ON_3dPoint const *', 'V')])
    cls.add_instance_attribute('vi', 'int [ 4 ]', is_const=False)
    return

def register_ON_MeshFaceSide_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshFaceSide const &', 'arg0')])
    cls.add_instance_attribute('dir', 'unsigned char', is_const=False)
    cls.add_instance_attribute('fi', 'int', is_const=False)
    cls.add_instance_attribute('side', 'unsigned char', is_const=False)
    cls.add_instance_attribute('value', 'short unsigned int', is_const=False)
    cls.add_instance_attribute('vi', 'int [ 2 ]', is_const=False)
    return

def register_ON_MeshNgon_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshNgon const &', 'arg0')])
    cls.add_instance_attribute('N', 'int', is_const=False)
    cls.add_instance_attribute('fi', 'int *', is_const=False)
    cls.add_instance_attribute('vi', 'int *', is_const=False)
    return

def register_ON_MeshNgonList_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshNgonList const &', 'arg0')])
    cls.add_method('AddNgon', 
                   'bool', 
                   [param('int', 'N'), param('int const *', 'vi'), param('int const *', 'fi')])
    cls.add_method('AddNgon', 
                   'ON_MeshNgon *', 
                   [param('int', 'N')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Ngon', 
                   'ON_MeshNgon *', 
                   [param('int', 'Ngon_index')], 
                   is_const=True)
    cls.add_method('NgonCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('ReserveNgonCapacity', 
                   'bool', 
                   [param('int', 'capacity')])
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    return

def register_ON_MeshParameters_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('==')
    cls.add_constructor([param('ON_MeshParameters const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_MeshParameters const &', 'arg0')], 
                   is_const=True)
    cls.add_method('CompareGeometrySettings', 
                   'int', 
                   [param('ON_MeshParameters const &', 'arg0')], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'arg0')], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('DefaultAnalysisMeshParameters', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'test_log')], 
                   is_const=True)
    cls.add_method('JaggedAndFasterMeshParameters', 
                   'void', 
                   [])
    cls.add_method('MinEdgeLength', 
                   'double', 
                   [param('double', 'max_edge_length'), param('double', 'tolerance')], 
                   is_static=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Set', 
                   'void', 
                   [param('double', 'density'), param('double', 'min_edge_length', default_value='1.00000000000000004792173602385929598312941379845e-4')])
    cls.add_method('SmoothAndSlowerMeshParameters', 
                   'void', 
                   [])
    cls.add_method('Tolerance', 
                   'double', 
                   [param('double', 'relative_tolerance'), param('double', 'actual_size')], 
                   is_static=True)
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_static_attribute('FastRenderMesh', 'ON_MeshParameters const', is_const=True)
    cls.add_static_attribute('QualityRenderMesh', 'ON_MeshParameters const', is_const=True)
    cls.add_instance_attribute('m_bComputeCurvature', 'bool', is_const=False)
    cls.add_instance_attribute('m_bCustomSettings', 'bool', is_const=False)
    cls.add_instance_attribute('m_bCustomSettingsEnabled', 'bool', is_const=False)
    cls.add_instance_attribute('m_bDoublePrecision', 'bool', is_const=False)
    cls.add_instance_attribute('m_bJaggedSeams', 'bool', is_const=False)
    cls.add_instance_attribute('m_bRefine', 'bool', is_const=False)
    cls.add_instance_attribute('m_bSimplePlanes', 'bool', is_const=False)
    cls.add_instance_attribute('m_face_type', 'int', is_const=False)
    cls.add_instance_attribute('m_grid_amplification', 'double', is_const=False)
    cls.add_instance_attribute('m_grid_angle', 'double', is_const=False)
    cls.add_instance_attribute('m_grid_aspect_ratio', 'double', is_const=False)
    cls.add_instance_attribute('m_grid_max_count', 'int', is_const=False)
    cls.add_instance_attribute('m_grid_min_count', 'int', is_const=False)
    cls.add_instance_attribute('m_max_edge_length', 'double', is_const=False)
    cls.add_instance_attribute('m_mesher', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_min_edge_length', 'double', is_const=False)
    cls.add_instance_attribute('m_min_tolerance', 'double', is_const=False)
    cls.add_instance_attribute('m_refine_angle', 'double', is_const=False)
    cls.add_instance_attribute('m_relative_tolerance', 'double', is_const=False)
    cls.add_instance_attribute('m_texture_range', 'int', is_const=False)
    cls.add_instance_attribute('m_tolerance', 'double', is_const=False)
    return

def register_ON_MeshPart_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshPart const &', 'arg0')])
    cls.add_instance_attribute('fi', 'int [ 2 ]', is_const=False)
    cls.add_instance_attribute('triangle_count', 'int', is_const=False)
    cls.add_instance_attribute('vertex_count', 'int', is_const=False)
    cls.add_instance_attribute('vi', 'int [ 2 ]', is_const=False)
    return

def register_ON_MeshPartition_methods(root_module, cls):
    cls.add_constructor([param('ON_MeshPartition const &', 'arg0')])
    cls.add_constructor([])
    cls.add_instance_attribute('m_part', 'ON_SimpleArray< ON_MeshPart >', is_const=False)
    cls.add_instance_attribute('m_partition_max_triangle_count', 'int', is_const=False)
    cls.add_instance_attribute('m_partition_max_vertex_count', 'int', is_const=False)
    return

def register_ON_MeshTopology_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('EdgeRef', 
                   'ON_MeshEdgeRef', 
                   [param('ON_COMPONENT_INDEX', 'ci')], 
                   is_const=True)
    cls.add_method('EdgeRef', 
                   'ON_MeshEdgeRef', 
                   [param('int', 'tope_index')], 
                   is_const=True)
    cls.add_method('FaceRef', 
                   'ON_MeshFaceRef', 
                   [param('ON_COMPONENT_INDEX', 'ci')], 
                   is_const=True)
    cls.add_method('FaceRef', 
                   'ON_MeshFaceRef', 
                   [param('int', 'topf_index')], 
                   is_const=True)
    cls.add_method('GetIntArray', 
                   'int *', 
                   [param('int', 'count')])
    cls.add_method('GetTopFaceVertices', 
                   'bool', 
                   [param('int', 'topfi'), param('int *', 'topvi')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('SortVertexEdges', 
                   'bool', 
                   [param('int', 'topvi')], 
                   is_const=True)
    cls.add_method('SortVertexEdges', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('TopEdge', 
                   'int', 
                   [param('int', 'vtopi0'), param('int', 'vtopi1')], 
                   is_const=True)
    cls.add_method('TopEdgeCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('TopEdgeIsHidden', 
                   'bool', 
                   [param('int', 'topei')], 
                   is_const=True)
    cls.add_method('TopEdgeLine', 
                   'ON_Line', 
                   [param('int', 'tope_index')], 
                   is_const=True)
    cls.add_method('TopFaceCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('TopFaceIsHidden', 
                   'bool', 
                   [param('int', 'topfi')], 
                   is_const=True)
    cls.add_method('TopVertexCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('TopVertexIsHidden', 
                   'bool', 
                   [param('int', 'topvi')], 
                   is_const=True)
    cls.add_method('TopVertexPoint', 
                   'ON_3fPoint', 
                   [param('int', 'topv_index')], 
                   is_const=True)
    cls.add_method('VertexRef', 
                   'ON_MeshVertexRef', 
                   [param('ON_COMPONENT_INDEX', 'ci')], 
                   is_const=True)
    cls.add_method('VertexRef', 
                   'ON_MeshVertexRef', 
                   [param('int', 'topv_index')], 
                   is_const=True)
    cls.add_instance_attribute('m_mesh', 'ON_Mesh const *', is_const=False)
    cls.add_instance_attribute('m_tope', 'ON_SimpleArray< ON_MeshTopologyEdge >', is_const=False)
    cls.add_instance_attribute('m_topf', 'ON_SimpleArray< ON_MeshTopologyFace >', is_const=False)
    cls.add_instance_attribute('m_topv', 'ON_SimpleArray< ON_MeshTopologyVertex >', is_const=False)
    cls.add_instance_attribute('m_topv_map', 'ON_SimpleArray< int >', is_const=False)
    return

def register_ON_MeshTopologyEdge_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshTopologyEdge const &', 'arg0')])
    cls.add_instance_attribute('m_topf_count', 'int', is_const=False)
    cls.add_instance_attribute('m_topfi', 'int const *', is_const=False)
    cls.add_instance_attribute('m_topvi', 'int [ 2 ]', is_const=False)
    return

def register_ON_MeshTopologyFace_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshTopologyFace const &', 'arg0')])
    cls.add_method('IsQuad', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsTriangle', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_instance_attribute('m_reve', 'char [ 4 ]', is_const=False)
    cls.add_instance_attribute('m_topei', 'int [ 4 ]', is_const=False)
    return

def register_ON_MeshTopologyVertex_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_MeshTopologyVertex const &', 'arg0')])
    cls.add_instance_attribute('m_tope_count', 'int', is_const=False)
    cls.add_instance_attribute('m_topei', 'int const *', is_const=False)
    cls.add_instance_attribute('m_v_count', 'int', is_const=False)
    cls.add_instance_attribute('m_vi', 'int const *', is_const=False)
    return

def register_ON_ObjRef_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_ObjRef const &', 'src')])
    cls.add_method('DecrementProxyReferenceCount', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('ProxyObject', 
                   'ON_Object const *', 
                   [param('int', 'proxy_object_index')], 
                   is_const=True)
    cls.add_method('ProxyReferenceCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('RemapObjectId', 
                   'void', 
                   [param('ON_SimpleArray< ON_UuidPair > const &', 'uuid_remap')])
    cls.add_method('SetParentIRef', 
                   'bool', 
                   [param('ON_InstanceRef const &', 'iref'), param('ON_UUID', 'iref_id'), param('int', 'idef_geometry_index')])
    cls.add_method('SetProxy', 
                   'void', 
                   [param('ON_Object *', 'proxy1'), param('ON_Object *', 'proxy2'), param('bool', 'bCountReferences')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m__iref', 'ON_SimpleArray< ON_ObjRef_IRefID >', is_const=False)
    cls.add_instance_attribute('m_component_index', 'ON_COMPONENT_INDEX', is_const=False)
    cls.add_instance_attribute('m_evp', 'ON_ObjRefEvaluationParameter', is_const=False)
    cls.add_instance_attribute('m_geometry', 'ON_Geometry const *', is_const=False)
    cls.add_instance_attribute('m_geometry_type', 'int', is_const=False)
    cls.add_instance_attribute('m_osnap_mode', 'ON::osnap_mode', is_const=False)
    cls.add_instance_attribute('m_parent_geometry', 'ON_Geometry const *', is_const=False)
    cls.add_instance_attribute('m_point', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_runtime_sn', 'unsigned int', is_const=False)
    cls.add_instance_attribute('m_uuid', 'ON_UUID', is_const=False)
    return

def register_ON_ObjRefEvaluationParameter_methods(root_module, cls):
    cls.add_constructor([param('ON_ObjRefEvaluationParameter const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_s', 'ON_Interval [ 3 ]', is_const=False)
    cls.add_instance_attribute('m_t', 'double [ 4 ]', is_const=False)
    cls.add_instance_attribute('m_t_ci', 'ON_COMPONENT_INDEX', is_const=False)
    cls.add_instance_attribute('m_t_type', 'int', is_const=False)
    return

def register_ON_ObjRef_IRefID_methods(root_module, cls):
    cls.add_constructor([param('ON_ObjRef_IRefID const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_component_index', 'ON_COMPONENT_INDEX', is_const=False)
    cls.add_instance_attribute('m_evp', 'ON_ObjRefEvaluationParameter', is_const=False)
    cls.add_instance_attribute('m_geometry_xform', 'ON_Xform', is_const=False)
    cls.add_instance_attribute('m_idef_geometry_index', 'int', is_const=False)
    cls.add_instance_attribute('m_idef_uuid', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_iref_uuid', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_iref_xform', 'ON_Xform', is_const=False)
    return

def register_ON_Object_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_Object const &', 'arg0')])
    cls.add_method('AttachUserData', 
                   'ON_BOOL32', 
                   [param('ON_UserData *', 'pUserData')])
    cls.add_method('Cast', 
                   'ON_Object *', 
                   [param('ON_Object *', 'arg0')], 
                   is_static=True)
    cls.add_method('Cast', 
                   'ON_Object const *', 
                   [param('ON_Object const *', 'arg0')], 
                   is_static=True)
    cls.add_method('ClassId', 
                   'ON_ClassId const *', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('CopyFrom', 
                   'bool', 
                   [param('ON_Object const *', 'src')])
    cls.add_method('CopyUserData', 
                   'void', 
                   [param('ON_Object const &', 'source_object')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True, is_virtual=True)
    cls.add_method('DestroyRuntimeCache', 
                   'void', 
                   [param('bool', 'bDelete', default_value='true')], 
                   is_virtual=True)
    cls.add_method('DetachUserData', 
                   'ON_BOOL32', 
                   [param('ON_UserData *', 'pUserData')])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Duplicate', 
                   'ON_Object *', 
                   [], 
                   is_const=True)
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('FirstUserData', 
                   'ON_UserData *', 
                   [], 
                   is_const=True)
    cls.add_method('GetUserData', 
                   'ON_UserData *', 
                   [param('ON_UUID const &', 'userdata_uuid')], 
                   is_const=True)
    cls.add_method('GetUserString', 
                   'bool', 
                   [param('wchar_t const *', 'key'), param('ON_wString &', 'string_value')], 
                   is_const=True)
    cls.add_method('GetUserStringKeys', 
                   'int', 
                   [param('ON_ClassArray< ON_wString > &', 'user_string_keys')], 
                   is_const=True)
    cls.add_method('GetUserStrings', 
                   'int', 
                   [param('ON_ClassArray< ON_UserString > &', 'user_strings')], 
                   is_const=True)
    cls.add_method('IsKindOf', 
                   'ON_BOOL32', 
                   [param('ON_ClassId const *', 'pClassId')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    cls.add_method('MemoryRelocate', 
                   'void', 
                   [], 
                   is_virtual=True)
    cls.add_method('ModelObjectId', 
                   'ON_UUID', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('MoveUserData', 
                   'void', 
                   [param('ON_Object &', 'source_object')])
    cls.add_method('ObjectType', 
                   'ON::object_type', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('PurgeUserData', 
                   'void', 
                   [])
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_virtual=True)
    cls.add_method('SetUserString', 
                   'bool', 
                   [param('wchar_t const *', 'key'), param('wchar_t const *', 'string_value')])
    cls.add_method('SetUserStrings', 
                   'int', 
                   [param('int', 'count'), param('ON_UserString const *', 'user_strings'), param('bool', 'bReplace')])
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('TransformUserData', 
                   'void', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('UserStringCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_const=True, is_virtual=True)
    cls.add_static_attribute('m_ON_Object_class_id', 'ON_ClassId const', is_const=True)
    cls.add_method('DuplicateObject', 
                   'ON_Object *', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_ON_ObjectArray__ON_BrepEdge_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_BrepEdge > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_BrepEdge *', 
                   [param('ON_BrepEdge *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepEdge const *, ON_BrepEdge const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_BrepFace_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_BrepFace > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_BrepFace *', 
                   [param('ON_BrepFace *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFace const *, ON_BrepFace const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_BrepFaceSide_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_BrepFaceSide > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_BrepFaceSide *', 
                   [param('ON_BrepFaceSide *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepFaceSide const *, ON_BrepFaceSide const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_BrepLoop_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_BrepLoop > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_BrepLoop *', 
                   [param('ON_BrepLoop *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepLoop const *, ON_BrepLoop const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_BrepRegion_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_BrepRegion > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_BrepRegion *', 
                   [param('ON_BrepRegion *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepRegion const *, ON_BrepRegion const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_BrepTrim_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_BrepTrim > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_BrepTrim *', 
                   [param('ON_BrepTrim *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepTrim const *, ON_BrepTrim const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_BrepVertex_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_BrepVertex > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_BrepVertex *', 
                   [param('ON_BrepVertex *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepVertex const *, ON_BrepVertex const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_DimStyle_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_DimStyle > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_DimStyle *', 
                   [param('ON_DimStyle *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_DimStyle const *, ON_DimStyle const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_Font_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_Font > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_Font *', 
                   [param('ON_Font *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Font const *, ON_Font const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_Group_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_Group > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_Group *', 
                   [param('ON_Group *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Group const *, ON_Group const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_HatchPattern_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_HatchPattern > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_HatchPattern *', 
                   [param('ON_HatchPattern *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchPattern const *, ON_HatchPattern const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_InstanceDefinition_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_InstanceDefinition > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_InstanceDefinition *', 
                   [param('ON_InstanceDefinition *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_InstanceDefinition const *, ON_InstanceDefinition const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_Layer_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_Layer > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_Layer *', 
                   [param('ON_Layer *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Layer const *, ON_Layer const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_Linetype_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_Linetype > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_Linetype *', 
                   [param('ON_Linetype *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Linetype const *, ON_Linetype const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_Material_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_Material > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_Material *', 
                   [param('ON_Material *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Material const *, ON_Material const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_Texture_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_Texture > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_Texture *', 
                   [param('ON_Texture *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Texture const *, ON_Texture const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_ObjectArray__ON_TextureMapping_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_ObjectArray< ON_TextureMapping > const &', 'src')])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Realloc', 
                   'ON_TextureMapping *', 
                   [param('ON_TextureMapping *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar')], 
                   is_virtual=True)
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_TextureMapping const *, ON_TextureMapping const * ) *', 'compar')], 
                   is_virtual=True)
    return

def register_ON_OffsetSurfaceFunction_methods(root_module, cls):
    cls.add_constructor([param('ON_OffsetSurfaceFunction const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('BaseSurface', 
                   'ON_Surface const *', 
                   [], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('DistanceAt', 
                   'double', 
                   [param('double', 's'), param('double', 't')], 
                   is_const=True)
    cls.add_method('EvaluateDistance', 
                   'bool', 
                   [param('double', 's'), param('double', 't'), param('int', 'num_der'), param('double *', 'value')], 
                   is_const=True)
    cls.add_method('OffsetDistance', 
                   'double', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('OffsetPointCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('OffsetSurfaceParameter', 
                   'ON_2dPoint', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 's'), param('double', 't')], 
                   is_const=True)
    cls.add_method('SetBaseSurface', 
                   'bool', 
                   [param('ON_Surface const *', 'srf')])
    cls.add_method('SetDistance', 
                   'bool', 
                   [param('int', 'index'), param('double', 'distance')])
    cls.add_method('SetOffsetPoint', 
                   'bool', 
                   [param('double', 's'), param('double', 't'), param('double', 'distance'), param('double', 'radius', default_value='0.0')])
    cls.add_method('SetPoint', 
                   'bool', 
                   [param('int', 'index'), param('double', 's'), param('double', 't')])
    cls.add_method('SetSideTangency', 
                   'bool', 
                   [param('int', 'side'), param('bool', 'bEnable')])
    cls.add_method('SideTangency', 
                   'bool', 
                   [param('int', 'side')], 
                   is_const=True)
    return

def register_ON_OffsetSurfaceValue_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_OffsetSurfaceValue const &', 'arg0')])
    cls.add_instance_attribute('m_distance', 'double', is_const=False)
    cls.add_instance_attribute('m_index', 'int', is_const=False)
    cls.add_instance_attribute('m_radius', 'double', is_const=False)
    cls.add_instance_attribute('m_s', 'double', is_const=False)
    cls.add_instance_attribute('m_t', 'double', is_const=False)
    return

def register_ON_Plane_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_Plane const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dPoint const &', 'origin'), param('ON_3dVector const &', 'normal')])
    cls.add_constructor([param('ON_3dPoint const &', 'origin'), param('ON_3dVector const &', 'x_dir'), param('ON_3dVector const &', 'y_dir')])
    cls.add_constructor([param('ON_3dPoint const &', 'origin'), param('ON_3dPoint const &', 'x_point'), param('ON_3dPoint const &', 'y_point')])
    cls.add_constructor([param('double const *', 'equation')])
    cls.add_method('ClosestPointTo', 
                   'bool', 
                   [param('ON_3dPoint', 'world_point'), param('double *', 'u'), param('double *', 'v')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'point')], 
                   is_const=True)
    cls.add_method('CreateFromEquation', 
                   'bool', 
                   [param('double const *', 'equation')])
    cls.add_method('CreateFromFrame', 
                   'bool', 
                   [param('ON_3dPoint const &', 'origin'), param('ON_3dVector const &', 'x_dir'), param('ON_3dVector const &', 'y_dir')])
    cls.add_method('CreateFromNormal', 
                   'bool', 
                   [param('ON_3dPoint const &', 'origin'), param('ON_3dVector const &', 'normal')])
    cls.add_method('CreateFromPoints', 
                   'bool', 
                   [param('ON_3dPoint const &', 'origin'), param('ON_3dPoint const &', 'point_on_x'), param('ON_3dPoint const &', 'point_on')])
    cls.add_method('DistanceTo', 
                   'double', 
                   [param('ON_3dPoint const &', 'point')], 
                   is_const=True)
    cls.add_method('Flip', 
                   'bool', 
                   [])
    cls.add_method('GetDistanceToBoundingBox', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'arg0'), param('double *', 'min'), param('double *', 'max')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsoLine', 
                   'ON_Line', 
                   [param('int', 'dir'), param('double', 'c')], 
                   is_const=True)
    cls.add_method('Normal', 
                   'ON_3dVector const &', 
                   [], 
                   is_const=True)
    cls.add_method('Origin', 
                   'ON_3dPoint const &', 
                   [], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'u'), param('double', 'v')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'u'), param('double', 'v'), param('double', 'w')], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle'), param('ON_3dVector const &', 'axis')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis'), param('ON_3dPoint const &', 'center')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle'), param('ON_3dVector const &', 'axis'), param('ON_3dPoint const &', 'center')])
    cls.add_method('SetOrigin', 
                   'void', 
                   [param('ON_3dPoint const &', 'origin')])
    cls.add_method('SwapCoordinates', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'delta')])
    cls.add_method('UpdateEquation', 
                   'bool', 
                   [])
    cls.add_method('Xaxis', 
                   'ON_3dVector const &', 
                   [], 
                   is_const=True)
    cls.add_method('Yaxis', 
                   'ON_3dVector const &', 
                   [], 
                   is_const=True)
    cls.add_static_attribute('World_xy', 'ON_Plane const', is_const=True)
    cls.add_instance_attribute('origin', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('plane_equation', 'ON_PlaneEquation', is_const=False)
    cls.add_instance_attribute('xaxis', 'ON_3dVector', is_const=False)
    cls.add_instance_attribute('yaxis', 'ON_3dVector', is_const=False)
    cls.add_instance_attribute('zaxis', 'ON_3dVector', is_const=False)
    return

def register_ON_PlaneEquation_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_PlaneEquation const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('double', 'xx'), param('double', 'yy'), param('double', 'zz'), param('double', 'dd')])
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'point')], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_3dPoint', 'P'), param('ON_3dVector', 'N')])
    cls.add_method('IsNearerThan', 
                   'bool', 
                   [param('ON_BezierCurve const &', 'bezcrv'), param('double', 's0'), param('double', 's1'), param('int', 'sample_count'), param('double', 'endpoint_tolerance'), param('double', 'interior_tolerance'), param('double *', 'smin'), param('double *', 'smax')], 
                   is_const=True)
    cls.add_method('IsSet', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumAbsoluteValueAt', 
                   'double', 
                   [param('bool', 'bRational'), param('int', 'point_count'), param('int', 'point_stride'), param('double const *', 'points'), param('double', 'stop_value')], 
                   is_const=True)
    cls.add_method('MaximumValueAt', 
                   'double', 
                   [param('ON_BoundingBox const &', 'bbox')], 
                   is_const=True)
    cls.add_method('MaximumValueAt', 
                   'double', 
                   [param('ON_CurveLeafBox const &', 'crvleafbox')], 
                   is_const=True)
    cls.add_method('MaximumValueAt', 
                   'double', 
                   [param('ON_SurfaceLeafBox const &', 'srfleafbox')], 
                   is_const=True)
    cls.add_method('MaximumValueAt', 
                   'double', 
                   [param('bool', 'bRational'), param('int', 'point_count'), param('int', 'point_stride'), param('double const *', 'points'), param('double', 'stop_value')], 
                   is_const=True)
    cls.add_method('MinimumValueAt', 
                   'double', 
                   [param('ON_BoundingBox const &', 'bbox')], 
                   is_const=True)
    cls.add_method('MinimumValueAt', 
                   'double', 
                   [param('ON_CurveLeafBox const &', 'crvleafbox')], 
                   is_const=True)
    cls.add_method('MinimumValueAt', 
                   'double', 
                   [param('ON_SurfaceLeafBox const &', 'srfleafbox')], 
                   is_const=True)
    cls.add_method('MinimumValueAt', 
                   'double', 
                   [param('bool', 'bRational'), param('int', 'point_count'), param('int', 'point_stride'), param('double const *', 'points'), param('double', 'stop_value')], 
                   is_const=True)
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'xform')])
    cls.add_method('ValueAt', 
                   'double', 
                   [param('ON_3dPoint', 'P')], 
                   is_const=True)
    cls.add_method('ValueAt', 
                   'double', 
                   [param('ON_4dPoint', 'P')], 
                   is_const=True)
    cls.add_method('ValueAt', 
                   'double', 
                   [param('ON_3dVector', 'P')], 
                   is_const=True)
    cls.add_method('ValueAt', 
                   'double', 
                   [param('double', 'x'), param('double', 'y'), param('double', 'z')], 
                   is_const=True)
    cls.add_method('ValueAt', 
                   'double *', 
                   [param('int', 'Pcount'), param('ON_3fPoint const *', 'P'), param('double *', 'value'), param('double *', 'value_range')], 
                   is_const=True)
    cls.add_method('ValueAt', 
                   'double *', 
                   [param('int', 'Pcount'), param('ON_3dPoint const *', 'P'), param('double *', 'value'), param('double *', 'value_range')], 
                   is_const=True)
    cls.add_method('ZeroTolerance', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_static_attribute('UnsetPlaneEquation', 'ON_PlaneEquation const', is_const=True)
    cls.add_static_attribute('ZeroPlaneEquation', 'ON_PlaneEquation const', is_const=True)
    cls.add_instance_attribute('d', 'double', is_const=False)
    return

def register_ON_PlugInRef_methods(root_module, cls):
    cls.add_constructor([param('ON_PlugInRef const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'file')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'file')], 
                   is_const=True)
    cls.add_instance_attribute('m_developer_address', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_developer_country', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_developer_email', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_developer_fax', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_developer_organization', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_developer_phone', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_developer_updateurl', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_developer_website', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_plugin_filename', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_plugin_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_plugin_name', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_plugin_platform', 'int', is_const=False)
    cls.add_instance_attribute('m_plugin_sdk_service_release', 'int', is_const=False)
    cls.add_instance_attribute('m_plugin_sdk_version', 'int', is_const=False)
    cls.add_instance_attribute('m_plugin_type', 'int', is_const=False)
    cls.add_instance_attribute('m_plugin_version', 'ON_wString', is_const=False)
    return

def register_ON_PolyEdgeHistory_methods(root_module, cls):
    cls.add_constructor([param('ON_PolyEdgeHistory const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_evaluation_mode', 'int', is_const=False)
    cls.add_instance_attribute('m_segment', 'ON_ClassArray< ON_CurveProxyHistory >', is_const=False)
    cls.add_instance_attribute('m_t', 'ON_SimpleArray< double >', is_const=False)
    return

def register_ON_PolynomialCurve_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'dim'), param('ON_BOOL32', 'bIsRational'), param('int', 'order')])
    cls.add_constructor([param('ON_PolynomialCurve const &', 'arg0')])
    cls.add_constructor([param('ON_BezierCurve const &', 'arg0')])
    cls.add_method('Create', 
                   'ON_BOOL32', 
                   [param('int', 'dim'), param('ON_BOOL32', 'bIsRational'), param('int', 'order')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Evaluate', 
                   'ON_BOOL32', 
                   [param('double', 't'), param('int', 'der_count'), param('int', 'v_stride'), param('double *', 'v')], 
                   is_const=True)
    cls.add_instance_attribute('m_cv', 'ON_4dPointArray', is_const=False)
    cls.add_instance_attribute('m_dim', 'int', is_const=False)
    cls.add_instance_attribute('m_domain', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('m_is_rat', 'int', is_const=False)
    cls.add_instance_attribute('m_order', 'int', is_const=False)
    return

def register_ON_PolynomialSurface_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0'), param('ON_BOOL32', 'arg1'), param('int', 'arg2'), param('int', 'arg3')])
    cls.add_constructor([param('ON_PolynomialSurface const &', 'arg0')])
    cls.add_constructor([param('ON_BezierSurface const &', 'arg0')])
    cls.add_method('Create', 
                   'ON_BOOL32', 
                   [param('int', 'arg0'), param('ON_BOOL32', 'arg1'), param('int', 'arg2'), param('int', 'arg3')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Evaluate', 
                   'ON_BOOL32', 
                   [param('double', 's'), param('double', 't'), param('int', 'der_count'), param('int', 'v_stride'), param('double *', 'v')], 
                   is_const=True)
    cls.add_instance_attribute('m_cv', 'ON_4dPointArray', is_const=False)
    cls.add_instance_attribute('m_dim', 'int', is_const=False)
    cls.add_instance_attribute('m_domain', 'ON_Interval [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_is_rat', 'int', is_const=False)
    cls.add_instance_attribute('m_order', 'int [ 2 ]', is_const=False)
    return

def register_ON_RANDOM_NUMBER_CONTEXT_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_RANDOM_NUMBER_CONTEXT const &', 'arg0')])
    cls.add_instance_attribute('mt', 'ON__UINT32 [ 624 ]', is_const=False)
    cls.add_instance_attribute('mti', 'ON__UINT32', is_const=False)
    return

def register_ON_RTree_methods(root_module, cls):
    cls.add_constructor([param('ON_RTree const &', 'arg0')])
    cls.add_constructor([param('void *', 'heap', default_value='0'), param('size_t', 'leaf_count', default_value='0')])
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('CreateMeshFaceTree', 
                   'bool', 
                   [param('ON_Mesh const *', 'mesh')])
    cls.add_method('ElementCount', 
                   'int', 
                   [])
    cls.add_method('Insert', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('void *', 'a_element_id')])
    cls.add_method('Insert', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('int', 'a_element_id')])
    cls.add_method('Insert2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('void *', 'a_element_id')])
    cls.add_method('Insert2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('int', 'a_element_id')])
    cls.add_method('Remove', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('void *', 'a_elementId')])
    cls.add_method('Remove', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('int', 'a_elementId')])
    cls.add_method('Remove2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('void *', 'a_elementId')])
    cls.add_method('Remove2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('int', 'a_elementId')])
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    cls.add_method('Root', 
                   'ON_RTreeNode const *', 
                   [], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('ON_RTreeSphere *', 'a_sphere'), param('bool ( * ) ( void *, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('ON_RTreeCapsule *', 'a_capsule'), param('bool ( * ) ( void *, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('ON_RTreeBBox *', 'a_rect'), param('bool ( * ) ( void *, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('double const *', 'a_plane_eqn'), param('double', 'a_min'), param('double', 'a_max'), param('bool ( * ) ( void *, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('bool ( * ) ( void *, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_RTreeSearchResult &', 'a_result')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_SimpleArray< ON_RTreeLeaf > &', 'a_result')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_SimpleArray< void * > &', 'a_result')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_SimpleArray< int > &', 'a_result')], 
                   is_const=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('ON_RTree const &', 'a_rtreeA'), param('ON_RTree const &', 'a_rtreeB'), param('double', 'tolerance'), param('ON_SimpleArray< tagON_2dex > &', 'a_result')], 
                   is_static=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('ON_RTree const &', 'a_rtreeA'), param('ON_RTree const &', 'a_rtreeB'), param('double', 'tolerance'), param('void ( * ) ( void *, ON__INT_PTR, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_static=True)
    cls.add_method('Search', 
                   'bool', 
                   [param('ON_RTree const &', 'a_rtreeA'), param('ON_RTree const &', 'a_rtreeB'), param('double', 'tolerance'), param('bool ( * ) ( void *, ON__INT_PTR, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_static=True)
    cls.add_method('Search2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('bool ( * ) ( void *, ON__INT_PTR ) *', 'resultCallback'), param('void *', 'a_context')], 
                   is_const=True)
    cls.add_method('Search2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_RTreeSearchResult &', 'a_result')], 
                   is_const=True)
    cls.add_method('Search2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_SimpleArray< ON_RTreeLeaf > &', 'a_result')], 
                   is_const=True)
    cls.add_method('Search2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_SimpleArray< void * > &', 'a_result')], 
                   is_const=True)
    cls.add_method('Search2d', 
                   'bool', 
                   [param('double const *', 'a_min'), param('double const *', 'a_max'), param('ON_SimpleArray< int > &', 'a_result')], 
                   is_const=True)
    cls.add_method('SizeOf', 
                   'size_t', 
                   [], 
                   is_const=True)
    return

def register_ON_RTreeBBox_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTreeBBox const &', 'arg0')])
    cls.add_instance_attribute('m_max', 'double [ 3 ]', is_const=False)
    cls.add_instance_attribute('m_min', 'double [ 3 ]', is_const=False)
    return

def register_ON_RTreeBranch_methods(root_module, cls):
    cls.add_instance_attribute('m_child', 'ON_RTreeNode *', is_const=False)
    cls.add_instance_attribute('m_id', 'ON__INT_PTR', is_const=False)
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTreeBranch const &', 'arg0')])
    cls.add_instance_attribute('m_rect', 'ON_RTreeBBox', is_const=False)
    return

def register_ON_RTreeCapsule_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTreeCapsule const &', 'arg0')])
    cls.add_instance_attribute('m_domain', 'double [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_point', 'double [ 3 ] [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_radius', 'double', is_const=False)
    return

def register_ON_RTreeIterator_methods(root_module, cls):
    cls.add_constructor([param('ON_RTreeIterator const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTree const &', 'a_rtree')])
    cls.add_method('First', 
                   'bool', 
                   [])
    cls.add_method('Initialize', 
                   'bool', 
                   [param('ON_RTree const &', 'a_rtree')])
    cls.add_method('Initialize', 
                   'bool', 
                   [param('ON_RTreeNode const *', 'a_node')])
    cls.add_method('Last', 
                   'bool', 
                   [])
    cls.add_method('Next', 
                   'bool', 
                   [])
    cls.add_method('Prev', 
                   'bool', 
                   [])
    cls.add_method('Value', 
                   'ON_RTreeBranch const *', 
                   [], 
                   is_const=True)
    return

def register_ON_RTreeLeaf_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTreeLeaf const &', 'arg0')])
    cls.add_instance_attribute('m_id', 'ON__INT_PTR', is_const=False)
    cls.add_instance_attribute('m_rect', 'ON_RTreeBBox', is_const=False)
    return

def register_ON_RTreeMemPool_methods(root_module, cls):
    cls.add_constructor([param('ON_RTreeMemPool const &', 'arg0')])
    cls.add_constructor([param('void *', 'heap'), param('size_t', 'leaf_count')])
    cls.add_method('AllocListNode', 
                   'ON_RTreeListNode *', 
                   [])
    cls.add_method('AllocNode', 
                   'ON_RTreeNode *', 
                   [])
    cls.add_method('DeallocateAll', 
                   'void', 
                   [])
    cls.add_method('FreeListNode', 
                   'void', 
                   [param('ON_RTreeListNode *', 'list_node')])
    cls.add_method('FreeNode', 
                   'void', 
                   [param('ON_RTreeNode *', 'node')])
    cls.add_method('SizeOf', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfUnusedBuffer', 
                   'size_t', 
                   [], 
                   is_const=True)
    return

def register_ON_RTreeNode_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTreeNode const &', 'arg0')])
    cls.add_method('IsInternalNode', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsLeaf', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_instance_attribute('m_branch', 'ON_RTreeBranch [ 6 ]', is_const=False)
    cls.add_instance_attribute('m_count', 'int', is_const=False)
    cls.add_instance_attribute('m_level', 'int', is_const=False)
    return

def register_ON_RTreeSearchResult_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTreeSearchResult const &', 'arg0')])
    cls.add_instance_attribute('m_capacity', 'int', is_const=False)
    cls.add_instance_attribute('m_count', 'int', is_const=False)
    cls.add_instance_attribute('m_id', 'ON__INT_PTR *', is_const=False)
    return

def register_ON_RTreeSphere_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_RTreeSphere const &', 'arg0')])
    cls.add_instance_attribute('m_point', 'double [ 3 ]', is_const=False)
    cls.add_instance_attribute('m_radius', 'double', is_const=False)
    return

def register_ON_RandomNumberGenerator_methods(root_module, cls):
    cls.add_constructor([param('ON_RandomNumberGenerator const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('RandomDouble', 
                   'double', 
                   [])
    cls.add_method('RandomDouble', 
                   'double', 
                   [param('double', 't0'), param('double', 't1')])
    cls.add_method('RandomNumber', 
                   'ON__UINT32', 
                   [])
    cls.add_method('RandomPermutation', 
                   'void', 
                   [param('void *', 'base'), param('size_t', 'nel'), param('size_t', 'sizeof_element')])
    cls.add_method('Seed', 
                   'void', 
                   [param('ON__UINT32', 's')])
    return

def register_ON_Read3dmBufferArchive_methods(root_module, cls):
    cls.add_constructor([param('size_t', 'sizeof_buffer'), param('void const *', 'buffer'), param('bool', 'bCopyBuffer'), param('int', 'archive_3dm_version'), param('int', 'archive_opennurbs_version')])
    cls.add_method('SizeOfBuffer', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('Buffer', 
                   'void const *', 
                   [], 
                   is_const=True)
    cls.add_method('CurrentPosition', 
                   'size_t', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('SeekFromCurrentPosition', 
                   'bool', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('SeekFromStart', 
                   'bool', 
                   [param('size_t', 'arg0')], 
                   is_virtual=True)
    cls.add_method('AtEnd', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Read', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void *', 'arg1')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('Write', 
                   'size_t', 
                   [param('size_t', 'arg0'), param('void const *', 'arg1')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('Flush', 
                   'bool', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_ON_RenderingAttributes_methods(root_module, cls):
    cls.add_constructor([param('ON_RenderingAttributes const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_RenderingAttributes const &', 'other')], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'text_log')], 
                   is_const=True)
    cls.add_method('MaterialRef', 
                   'ON_MaterialRef const *', 
                   [param('ON_UUID const &', 'plugin_id')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'archive')], 
                   is_const=True)
    cls.add_instance_attribute('m_materials', 'ON_ClassArray< ON_MaterialRef >', is_const=False)
    return

def register_ON_SSX_EVENT_methods(root_module, cls):
    cls.add_constructor([param('ON_SSX_EVENT const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('IsCurveEvent', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsOverlapEvent', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsPointEvent', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsTangentEvent', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsTinyEvent', 
                   'bool', 
                   [param('double', 'tiny_tolerance')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'text_log'), param('double', 'intersection_tolerance'), param('double', 'overlap_tolerance'), param('double', 'fitting_tolerance'), param('ON_Surface const *', 'surfaceA'), param('ON_Interval const *', 'surfaceA_domain0'), param('ON_Interval const *', 'surfaceA_domain1'), param('ON_Surface const *', 'surfaceB'), param('ON_Interval const *', 'surfaceB_domain0'), param('ON_Interval const *', 'surfaceB_domain1')], 
                   is_const=True)
    cls.add_instance_attribute('m_curve3d', 'ON_Curve *', is_const=False)
    cls.add_instance_attribute('m_curveA', 'ON_Curve *', is_const=False)
    cls.add_instance_attribute('m_curveB', 'ON_Curve *', is_const=False)
    cls.add_instance_attribute('m_point3d', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_pointA', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_pointB', 'ON_3dPoint', is_const=False)
    cls.add_instance_attribute('m_type', 'ON_SSX_EVENT::TYPE', is_const=False)
    cls.add_instance_attribute('m_user', 'ON_U', is_const=False)
    return

def register_ON_SerialNumberMap_methods(root_module, cls):
    cls.add_constructor([param('void *', 'pool', default_value='0')])
    cls.add_method('ActiveIdCount', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('ActiveSerialNumberCount', 
                   'size_t', 
                   [], 
                   is_const=True)
    cls.add_method('AddSerialNumber', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [param('unsigned int', 'sn')])
    cls.add_method('AddSerialNumberAndId', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [param('unsigned int', 'sn'), param('ON_UUID', 'id')])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('EmptyList', 
                   'void', 
                   [])
    cls.add_method('FindId', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [param('ON_UUID', 'arg0')], 
                   is_const=True)
    cls.add_method('FindSerialNumber', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [param('unsigned int', 'sn')], 
                   is_const=True)
    cls.add_method('FirstElement', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [], 
                   is_const=True)
    cls.add_method('GetElements', 
                   'size_t', 
                   [param('unsigned int', 'sn0'), param('unsigned int', 'sn1'), param('size_t', 'max_count'), param('ON_SimpleArray< ON_SerialNumberMap::SN_ELEMENT > &', 'elements')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [param('ON_TextLog *', 'textlog')], 
                   is_const=True)
    cls.add_method('LastElement', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [], 
                   is_const=True)
    cls.add_method('RemoveId', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [param('unsigned int', 'sn'), param('ON_UUID', 'id')])
    cls.add_method('RemoveSerialNumberAndId', 
                   'ON_SerialNumberMap::SN_ELEMENT *', 
                   [param('unsigned int', 'sn')])
    return

def register_ON_SerialNumberMapMAP_VALUE_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_SerialNumberMap::MAP_VALUE const &', 'arg0')])
    cls.add_instance_attribute('i', 'int', is_const=False)
    cls.add_instance_attribute('ptr', 'void *', is_const=False)
    cls.add_instance_attribute('ui', 'unsigned int', is_const=False)
    cls.add_constructor([])
    cls.add_constructor([param('ON_SerialNumberMap::MAP_VALUE const &', 'arg0')])
    cls.add_instance_attribute('m_u_type', 'ON__UINT32', is_const=False)
    return

def register_ON_SerialNumberMapSN_ELEMENT_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_SerialNumberMap::SN_ELEMENT const &', 'arg0')])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_id_active', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_next', 'ON_SerialNumberMap::SN_ELEMENT *', is_const=False)
    cls.add_instance_attribute('m_reserved1', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_reserved2', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_sn', 'unsigned int', is_const=False)
    cls.add_instance_attribute('m_sn_active', 'unsigned char', is_const=False)
    cls.add_instance_attribute('m_value', 'ON_SerialNumberMap::MAP_VALUE', is_const=False)
    return

def register_ON_SimpleArray__ON_2dPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_2dPoint > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_2dPoint const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2dPoint const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_2dPoint &', 
                   [])
    cls.add_method('Array', 
                   'ON_2dPoint *', 
                   [])
    cls.add_method('Array', 
                   'ON_2dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dPoint *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_2dPoint *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_2dPoint *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2dPoint *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2dPoint const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dPoint const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dPoint const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dPoint const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2dPoint const *', 'arg0'), param('int ( * ) ( ON_2dPoint const *, ON_2dPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2dPoint const *', 'arg0'), param('int ( * ) ( ON_2dPoint const *, ON_2dPoint const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_2dPoint *', 
                   [])
    cls.add_method('First', 
                   'ON_2dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2dPoint const *, ON_2dPoint const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2dPoint const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_2dPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_2dPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_2dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2dPoint const *, ON_2dPoint const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_2dPoint *', 
                   [param('ON_2dPoint *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2dPoint const *', 'arg0'), param('int ( * ) ( ON_2dPoint const *, ON_2dPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2dPoint *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2dPoint *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2dPoint const *, ON_2dPoint const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2dPoint const *, ON_2dPoint const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_2dVector_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_2dVector > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_2dVector const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2dVector const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_2dVector &', 
                   [])
    cls.add_method('Array', 
                   'ON_2dVector *', 
                   [])
    cls.add_method('Array', 
                   'ON_2dVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dVector *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_2dVector *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_2dVector *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2dVector *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2dVector const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dVector const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dVector const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2dVector const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2dVector const *', 'arg0'), param('int ( * ) ( ON_2dVector const *, ON_2dVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2dVector const *', 'arg0'), param('int ( * ) ( ON_2dVector const *, ON_2dVector const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_2dVector *', 
                   [])
    cls.add_method('First', 
                   'ON_2dVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2dVector const *, ON_2dVector const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2dVector const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_2dVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_2dVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_2dVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2dVector const *, ON_2dVector const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_2dVector *', 
                   [param('ON_2dVector *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2dVector const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2dVector const *', 'arg0'), param('int ( * ) ( ON_2dVector const *, ON_2dVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2dVector *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2dVector *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2dVector const *, ON_2dVector const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2dVector const *, ON_2dVector const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_2fPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_2fPoint > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_2fPoint const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2fPoint const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_2fPoint &', 
                   [])
    cls.add_method('Array', 
                   'ON_2fPoint *', 
                   [])
    cls.add_method('Array', 
                   'ON_2fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fPoint *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_2fPoint *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_2fPoint *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2fPoint *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2fPoint const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fPoint const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fPoint const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fPoint const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2fPoint const *', 'arg0'), param('int ( * ) ( ON_2fPoint const *, ON_2fPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2fPoint const *', 'arg0'), param('int ( * ) ( ON_2fPoint const *, ON_2fPoint const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_2fPoint *', 
                   [])
    cls.add_method('First', 
                   'ON_2fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2fPoint const *, ON_2fPoint const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2fPoint const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_2fPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_2fPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_2fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2fPoint const *, ON_2fPoint const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_2fPoint *', 
                   [param('ON_2fPoint *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2fPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2fPoint const *', 'arg0'), param('int ( * ) ( ON_2fPoint const *, ON_2fPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2fPoint *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2fPoint *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2fPoint const *, ON_2fPoint const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2fPoint const *, ON_2fPoint const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_2fVector_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_2fVector > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_2fVector const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2fVector const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_2fVector &', 
                   [])
    cls.add_method('Array', 
                   'ON_2fVector *', 
                   [])
    cls.add_method('Array', 
                   'ON_2fVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fVector *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_2fVector *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_2fVector *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2fVector *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_2fVector const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fVector const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fVector const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_2fVector const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2fVector const *', 'arg0'), param('int ( * ) ( ON_2fVector const *, ON_2fVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_2fVector const *', 'arg0'), param('int ( * ) ( ON_2fVector const *, ON_2fVector const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_2fVector *', 
                   [])
    cls.add_method('First', 
                   'ON_2fVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2fVector const *, ON_2fVector const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_2fVector const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_2fVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_2fVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_2fVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_2fVector const *, ON_2fVector const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_2fVector *', 
                   [param('ON_2fVector *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2fVector const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_2fVector const *', 'arg0'), param('int ( * ) ( ON_2fVector const *, ON_2fVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2fVector *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_2fVector *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2fVector const *, ON_2fVector const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_2fVector const *, ON_2fVector const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_3DM_BIG_CHUNK_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_3DM_BIG_CHUNK > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_3DM_BIG_CHUNK *', 
                   [])
    cls.add_method('First', 
                   'ON_3DM_BIG_CHUNK const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3DM_BIG_CHUNK const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_3DM_BIG_CHUNK *', 
                   [])
    cls.add_method('Last', 
                   'ON_3DM_BIG_CHUNK const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_3DM_BIG_CHUNK &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_3DM_BIG_CHUNK const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_3DM_BIG_CHUNK const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_3DM_BIG_CHUNK const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3DM_BIG_CHUNK const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3DM_BIG_CHUNK const *', 'key'), param('int ( * ) ( ON_3DM_BIG_CHUNK const *, ON_3DM_BIG_CHUNK const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3DM_BIG_CHUNK const *', 'key'), param('int ( * ) ( ON_3DM_BIG_CHUNK const *, ON_3DM_BIG_CHUNK const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3DM_BIG_CHUNK const *', 'arg0'), param('int ( * ) ( ON_3DM_BIG_CHUNK const *, ON_3DM_BIG_CHUNK const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3DM_BIG_CHUNK const *, ON_3DM_BIG_CHUNK const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3DM_BIG_CHUNK const *, ON_3DM_BIG_CHUNK const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_3DM_BIG_CHUNK const *, ON_3DM_BIG_CHUNK const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_3DM_BIG_CHUNK const *, ON_3DM_BIG_CHUNK const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_3DM_BIG_CHUNK *', 
                   [param('ON_3DM_BIG_CHUNK *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_3DM_BIG_CHUNK *', 
                   [])
    cls.add_method('Array', 
                   'ON_3DM_BIG_CHUNK const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_3DM_BIG_CHUNK *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3DM_BIG_CHUNK *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3DM_BIG_CHUNK *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_3dPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_3dPoint > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_3dPoint const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3dPoint const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_3dPoint &', 
                   [])
    cls.add_method('Array', 
                   'ON_3dPoint *', 
                   [])
    cls.add_method('Array', 
                   'ON_3dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dPoint *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_3dPoint *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_3dPoint *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3dPoint *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3dPoint const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dPoint const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dPoint const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dPoint const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dPoint const *', 'arg0'), param('int ( * ) ( ON_3dPoint const *, ON_3dPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dPoint const *', 'arg0'), param('int ( * ) ( ON_3dPoint const *, ON_3dPoint const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_3dPoint *', 
                   [])
    cls.add_method('First', 
                   'ON_3dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dPoint const *, ON_3dPoint const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3dPoint const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_3dPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_3dPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_3dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dPoint const *, ON_3dPoint const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_3dPoint *', 
                   [param('ON_3dPoint *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3dPoint const *', 'arg0'), param('int ( * ) ( ON_3dPoint const *, ON_3dPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dPoint *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dPoint *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3dPoint const *, ON_3dPoint const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3dPoint const *, ON_3dPoint const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_3dVector_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_3dVector > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3dVector const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_3dVector &', 
                   [])
    cls.add_method('Array', 
                   'ON_3dVector *', 
                   [])
    cls.add_method('Array', 
                   'ON_3dVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dVector *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_3dVector *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_3dVector *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3dVector *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3dVector const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dVector const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dVector const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3dVector const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dVector const *', 'arg0'), param('int ( * ) ( ON_3dVector const *, ON_3dVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3dVector const *', 'arg0'), param('int ( * ) ( ON_3dVector const *, ON_3dVector const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_3dVector *', 
                   [])
    cls.add_method('First', 
                   'ON_3dVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dVector const *, ON_3dVector const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3dVector const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_3dVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_3dVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_3dVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3dVector const *, ON_3dVector const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_3dVector *', 
                   [param('ON_3dVector *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3dVector const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3dVector const *', 'arg0'), param('int ( * ) ( ON_3dVector const *, ON_3dVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dVector *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3dVector *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3dVector const *, ON_3dVector const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3dVector const *, ON_3dVector const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_3fPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_3fPoint > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_3fPoint const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3fPoint const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_3fPoint &', 
                   [])
    cls.add_method('Array', 
                   'ON_3fPoint *', 
                   [])
    cls.add_method('Array', 
                   'ON_3fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fPoint *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_3fPoint *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_3fPoint *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3fPoint *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3fPoint const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fPoint const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fPoint const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fPoint const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3fPoint const *', 'arg0'), param('int ( * ) ( ON_3fPoint const *, ON_3fPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3fPoint const *', 'arg0'), param('int ( * ) ( ON_3fPoint const *, ON_3fPoint const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_3fPoint *', 
                   [])
    cls.add_method('First', 
                   'ON_3fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3fPoint const *, ON_3fPoint const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3fPoint const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_3fPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_3fPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_3fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3fPoint const *, ON_3fPoint const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_3fPoint *', 
                   [param('ON_3fPoint *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3fPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3fPoint const *', 'arg0'), param('int ( * ) ( ON_3fPoint const *, ON_3fPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3fPoint *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3fPoint *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3fPoint const *, ON_3fPoint const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3fPoint const *, ON_3fPoint const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_3fVector_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_3fVector > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_3fVector const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3fVector const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_3fVector &', 
                   [])
    cls.add_method('Array', 
                   'ON_3fVector *', 
                   [])
    cls.add_method('Array', 
                   'ON_3fVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fVector *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_3fVector *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_3fVector *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3fVector *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_3fVector const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fVector const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fVector const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_3fVector const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3fVector const *', 'arg0'), param('int ( * ) ( ON_3fVector const *, ON_3fVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_3fVector const *', 'arg0'), param('int ( * ) ( ON_3fVector const *, ON_3fVector const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_3fVector *', 
                   [])
    cls.add_method('First', 
                   'ON_3fVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3fVector const *, ON_3fVector const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_3fVector const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_3fVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_3fVector *', 
                   [])
    cls.add_method('Last', 
                   'ON_3fVector const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_3fVector const *, ON_3fVector const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_3fVector *', 
                   [param('ON_3fVector *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3fVector const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_3fVector const *', 'arg0'), param('int ( * ) ( ON_3fVector const *, ON_3fVector const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3fVector *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_3fVector *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3fVector const *, ON_3fVector const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_3fVector const *, ON_3fVector const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_4dPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_4dPoint > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_4dPoint const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_4dPoint const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_4dPoint &', 
                   [])
    cls.add_method('Array', 
                   'ON_4dPoint *', 
                   [])
    cls.add_method('Array', 
                   'ON_4dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4dPoint *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_4dPoint *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_4dPoint *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_4dPoint *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_4dPoint const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4dPoint const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4dPoint const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4dPoint const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_4dPoint const *', 'arg0'), param('int ( * ) ( ON_4dPoint const *, ON_4dPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_4dPoint const *', 'arg0'), param('int ( * ) ( ON_4dPoint const *, ON_4dPoint const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_4dPoint *', 
                   [])
    cls.add_method('First', 
                   'ON_4dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_4dPoint const *, ON_4dPoint const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_4dPoint const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_4dPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_4dPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_4dPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_4dPoint const *, ON_4dPoint const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_4dPoint *', 
                   [param('ON_4dPoint *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_4dPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_4dPoint const *', 'arg0'), param('int ( * ) ( ON_4dPoint const *, ON_4dPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_4dPoint *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_4dPoint *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_4dPoint const *, ON_4dPoint const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_4dPoint const *, ON_4dPoint const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_4fPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_4fPoint > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_4fPoint const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_4fPoint const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_4fPoint &', 
                   [])
    cls.add_method('Array', 
                   'ON_4fPoint *', 
                   [])
    cls.add_method('Array', 
                   'ON_4fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4fPoint *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_4fPoint *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_4fPoint *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_4fPoint *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_4fPoint const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4fPoint const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4fPoint const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_4fPoint const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_4fPoint const *', 'arg0'), param('int ( * ) ( ON_4fPoint const *, ON_4fPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_4fPoint const *', 'arg0'), param('int ( * ) ( ON_4fPoint const *, ON_4fPoint const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_4fPoint *', 
                   [])
    cls.add_method('First', 
                   'ON_4fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_4fPoint const *, ON_4fPoint const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_4fPoint const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_4fPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_4fPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_4fPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_4fPoint const *, ON_4fPoint const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_4fPoint *', 
                   [param('ON_4fPoint *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_4fPoint const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_4fPoint const *', 'arg0'), param('int ( * ) ( ON_4fPoint const *, ON_4fPoint const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_4fPoint *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_4fPoint *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_4fPoint const *, ON_4fPoint const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_4fPoint const *, ON_4fPoint const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_Bitmap__star___methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_Bitmap * > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Bitmap * *', 
                   [])
    cls.add_method('First', 
                   'ON_Bitmap * const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Bitmap * *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Bitmap * *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Bitmap * *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Bitmap * *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Bitmap * const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Bitmap * const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Bitmap * const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Bitmap * const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Bitmap * *', 
                   [])
    cls.add_method('Last', 
                   'ON_Bitmap * const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Bitmap * &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Bitmap * const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Bitmap * const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Bitmap * const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Bitmap * const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Bitmap * const *', 'key'), param('int ( * ) ( ON_Bitmap * const *, ON_Bitmap * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Bitmap * const *', 'key'), param('int ( * ) ( ON_Bitmap * const *, ON_Bitmap * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Bitmap * const *', 'arg0'), param('int ( * ) ( ON_Bitmap * const *, ON_Bitmap * const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Bitmap * const *, ON_Bitmap * const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Bitmap * const *, ON_Bitmap * const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Bitmap * const *, ON_Bitmap * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Bitmap * const *, ON_Bitmap * const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Bitmap * *', 
                   [param('ON_Bitmap * *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Bitmap * *', 
                   [])
    cls.add_method('Array', 
                   'ON_Bitmap * const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Bitmap * *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Bitmap * *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Bitmap * *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_BrepTrimPoint_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_BrepTrimPoint > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BrepTrimPoint *', 
                   [])
    cls.add_method('First', 
                   'ON_BrepTrimPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrimPoint *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrimPoint *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrimPoint *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrimPoint *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BrepTrimPoint const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrimPoint const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrimPoint const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BrepTrimPoint const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BrepTrimPoint *', 
                   [])
    cls.add_method('Last', 
                   'ON_BrepTrimPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BrepTrimPoint &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BrepTrimPoint const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BrepTrimPoint const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BrepTrimPoint const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepTrimPoint const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BrepTrimPoint const *', 'key'), param('int ( * ) ( ON_BrepTrimPoint const *, ON_BrepTrimPoint const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepTrimPoint const *', 'key'), param('int ( * ) ( ON_BrepTrimPoint const *, ON_BrepTrimPoint const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BrepTrimPoint const *', 'arg0'), param('int ( * ) ( ON_BrepTrimPoint const *, ON_BrepTrimPoint const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepTrimPoint const *, ON_BrepTrimPoint const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BrepTrimPoint const *, ON_BrepTrimPoint const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepTrimPoint const *, ON_BrepTrimPoint const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BrepTrimPoint const *, ON_BrepTrimPoint const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BrepTrimPoint *', 
                   [param('ON_BrepTrimPoint *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BrepTrimPoint *', 
                   [])
    cls.add_method('Array', 
                   'ON_BrepTrimPoint const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BrepTrimPoint *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepTrimPoint *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BrepTrimPoint *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_BumpFunction_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_BumpFunction > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_BumpFunction *', 
                   [])
    cls.add_method('First', 
                   'ON_BumpFunction const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BumpFunction *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_BumpFunction *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_BumpFunction *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_BumpFunction *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_BumpFunction const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BumpFunction const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BumpFunction const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_BumpFunction const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_BumpFunction *', 
                   [])
    cls.add_method('Last', 
                   'ON_BumpFunction const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_BumpFunction &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_BumpFunction const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_BumpFunction const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_BumpFunction const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BumpFunction const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_BumpFunction const *', 'key'), param('int ( * ) ( ON_BumpFunction const *, ON_BumpFunction const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BumpFunction const *', 'key'), param('int ( * ) ( ON_BumpFunction const *, ON_BumpFunction const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_BumpFunction const *', 'arg0'), param('int ( * ) ( ON_BumpFunction const *, ON_BumpFunction const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BumpFunction const *, ON_BumpFunction const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_BumpFunction const *, ON_BumpFunction const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BumpFunction const *, ON_BumpFunction const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_BumpFunction const *, ON_BumpFunction const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_BumpFunction *', 
                   [param('ON_BumpFunction *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_BumpFunction *', 
                   [])
    cls.add_method('Array', 
                   'ON_BumpFunction const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_BumpFunction *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BumpFunction *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_BumpFunction *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_ClippingPlaneInfo_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_ClippingPlaneInfo > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_ClippingPlaneInfo *', 
                   [])
    cls.add_method('First', 
                   'ON_ClippingPlaneInfo const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ClippingPlaneInfo const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_ClippingPlaneInfo *', 
                   [])
    cls.add_method('Last', 
                   'ON_ClippingPlaneInfo const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_ClippingPlaneInfo &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_ClippingPlaneInfo const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_ClippingPlaneInfo const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_ClippingPlaneInfo const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_ClippingPlaneInfo const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_ClippingPlaneInfo const *', 'key'), param('int ( * ) ( ON_ClippingPlaneInfo const *, ON_ClippingPlaneInfo const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_ClippingPlaneInfo const *', 'key'), param('int ( * ) ( ON_ClippingPlaneInfo const *, ON_ClippingPlaneInfo const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_ClippingPlaneInfo const *', 'arg0'), param('int ( * ) ( ON_ClippingPlaneInfo const *, ON_ClippingPlaneInfo const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_ClippingPlaneInfo const *, ON_ClippingPlaneInfo const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_ClippingPlaneInfo const *, ON_ClippingPlaneInfo const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_ClippingPlaneInfo const *, ON_ClippingPlaneInfo const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_ClippingPlaneInfo const *, ON_ClippingPlaneInfo const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_ClippingPlaneInfo *', 
                   [param('ON_ClippingPlaneInfo *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_ClippingPlaneInfo *', 
                   [])
    cls.add_method('Array', 
                   'ON_ClippingPlaneInfo const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_ClippingPlaneInfo *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_ClippingPlaneInfo *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_ClippingPlaneInfo *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_Color_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_Color > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Color *', 
                   [])
    cls.add_method('First', 
                   'ON_Color const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Color *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Color *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Color *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Color *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Color const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Color const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Color const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Color const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Color *', 
                   [])
    cls.add_method('Last', 
                   'ON_Color const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Color &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Color const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Color const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Color const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Color const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Color const *', 'key'), param('int ( * ) ( ON_Color const *, ON_Color const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Color const *', 'key'), param('int ( * ) ( ON_Color const *, ON_Color const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Color const *', 'arg0'), param('int ( * ) ( ON_Color const *, ON_Color const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Color const *, ON_Color const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Color const *, ON_Color const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Color const *, ON_Color const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Color const *, ON_Color const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Color *', 
                   [param('ON_Color *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Color *', 
                   [])
    cls.add_method('Array', 
                   'ON_Color const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Color *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Color *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Color *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_Curve__star___methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_Curve * > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Curve * *', 
                   [])
    cls.add_method('First', 
                   'ON_Curve * const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Curve * *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Curve * *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Curve * *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Curve * *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Curve * const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Curve * const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Curve * const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Curve * const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Curve * *', 
                   [])
    cls.add_method('Last', 
                   'ON_Curve * const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Curve * &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Curve * const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Curve * const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Curve * const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Curve * const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Curve * const *', 'key'), param('int ( * ) ( ON_Curve * const *, ON_Curve * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Curve * const *', 'key'), param('int ( * ) ( ON_Curve * const *, ON_Curve * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Curve * const *', 'arg0'), param('int ( * ) ( ON_Curve * const *, ON_Curve * const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Curve * const *, ON_Curve * const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Curve * const *, ON_Curve * const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Curve * const *, ON_Curve * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Curve * const *, ON_Curve * const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Curve * *', 
                   [param('ON_Curve * *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Curve * *', 
                   [])
    cls.add_method('Array', 
                   'ON_Curve * const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Curve * *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Curve * *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Curve * *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_DisplayMaterialRef_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_DisplayMaterialRef > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_DisplayMaterialRef *', 
                   [])
    cls.add_method('First', 
                   'ON_DisplayMaterialRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DisplayMaterialRef *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_DisplayMaterialRef *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_DisplayMaterialRef *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_DisplayMaterialRef *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_DisplayMaterialRef const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DisplayMaterialRef const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DisplayMaterialRef const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_DisplayMaterialRef const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_DisplayMaterialRef *', 
                   [])
    cls.add_method('Last', 
                   'ON_DisplayMaterialRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_DisplayMaterialRef &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_DisplayMaterialRef const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_DisplayMaterialRef const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_DisplayMaterialRef const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_DisplayMaterialRef const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_DisplayMaterialRef const *', 'key'), param('int ( * ) ( ON_DisplayMaterialRef const *, ON_DisplayMaterialRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_DisplayMaterialRef const *', 'key'), param('int ( * ) ( ON_DisplayMaterialRef const *, ON_DisplayMaterialRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_DisplayMaterialRef const *', 'arg0'), param('int ( * ) ( ON_DisplayMaterialRef const *, ON_DisplayMaterialRef const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_DisplayMaterialRef const *, ON_DisplayMaterialRef const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_DisplayMaterialRef const *, ON_DisplayMaterialRef const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_DisplayMaterialRef const *, ON_DisplayMaterialRef const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_DisplayMaterialRef const *, ON_DisplayMaterialRef const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_DisplayMaterialRef *', 
                   [param('ON_DisplayMaterialRef *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_DisplayMaterialRef *', 
                   [])
    cls.add_method('Array', 
                   'ON_DisplayMaterialRef const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_DisplayMaterialRef *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_DisplayMaterialRef *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_DisplayMaterialRef *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_HatchLoop__star___methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_HatchLoop * > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_HatchLoop * *', 
                   [])
    cls.add_method('First', 
                   'ON_HatchLoop * const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLoop * *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_HatchLoop * *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_HatchLoop * *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_HatchLoop * *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_HatchLoop * const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLoop * const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLoop * const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HatchLoop * const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_HatchLoop * *', 
                   [])
    cls.add_method('Last', 
                   'ON_HatchLoop * const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_HatchLoop * &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_HatchLoop * const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_HatchLoop * const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_HatchLoop * const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_HatchLoop * const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_HatchLoop * const *', 'key'), param('int ( * ) ( ON_HatchLoop * const *, ON_HatchLoop * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HatchLoop * const *', 'key'), param('int ( * ) ( ON_HatchLoop * const *, ON_HatchLoop * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HatchLoop * const *', 'arg0'), param('int ( * ) ( ON_HatchLoop * const *, ON_HatchLoop * const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchLoop * const *, ON_HatchLoop * const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HatchLoop * const *, ON_HatchLoop * const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HatchLoop * const *, ON_HatchLoop * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HatchLoop * const *, ON_HatchLoop * const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_HatchLoop * *', 
                   [param('ON_HatchLoop * *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_HatchLoop * *', 
                   [])
    cls.add_method('Array', 
                   'ON_HatchLoop * const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_HatchLoop * *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HatchLoop * *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HatchLoop * *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_HistoryRecord__star___methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_HistoryRecord * > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_HistoryRecord * *', 
                   [])
    cls.add_method('First', 
                   'ON_HistoryRecord * const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HistoryRecord * *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_HistoryRecord * *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_HistoryRecord * *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_HistoryRecord * *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_HistoryRecord * const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HistoryRecord * const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HistoryRecord * const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_HistoryRecord * const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_HistoryRecord * *', 
                   [])
    cls.add_method('Last', 
                   'ON_HistoryRecord * const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_HistoryRecord * &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_HistoryRecord * const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_HistoryRecord * const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_HistoryRecord * const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_HistoryRecord * const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_HistoryRecord * const *', 'key'), param('int ( * ) ( ON_HistoryRecord * const *, ON_HistoryRecord * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HistoryRecord * const *', 'key'), param('int ( * ) ( ON_HistoryRecord * const *, ON_HistoryRecord * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_HistoryRecord * const *', 'arg0'), param('int ( * ) ( ON_HistoryRecord * const *, ON_HistoryRecord * const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HistoryRecord * const *, ON_HistoryRecord * const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_HistoryRecord * const *, ON_HistoryRecord * const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HistoryRecord * const *, ON_HistoryRecord * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_HistoryRecord * const *, ON_HistoryRecord * const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_HistoryRecord * *', 
                   [param('ON_HistoryRecord * *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_HistoryRecord * *', 
                   [])
    cls.add_method('Array', 
                   'ON_HistoryRecord * const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_HistoryRecord * *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HistoryRecord * *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_HistoryRecord * *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_Interval_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_Interval > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Interval *', 
                   [])
    cls.add_method('First', 
                   'ON_Interval const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Interval *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Interval *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Interval *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Interval *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Interval const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Interval const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Interval const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Interval const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Interval *', 
                   [])
    cls.add_method('Last', 
                   'ON_Interval const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Interval &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Interval const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Interval const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Interval const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Interval const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Interval const *', 'key'), param('int ( * ) ( ON_Interval const *, ON_Interval const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Interval const *', 'key'), param('int ( * ) ( ON_Interval const *, ON_Interval const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Interval const *', 'arg0'), param('int ( * ) ( ON_Interval const *, ON_Interval const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Interval const *, ON_Interval const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Interval const *, ON_Interval const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Interval const *, ON_Interval const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Interval const *, ON_Interval const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Interval *', 
                   [param('ON_Interval *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Interval *', 
                   [])
    cls.add_method('Array', 
                   'ON_Interval const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Interval *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Interval *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Interval *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_LinetypeSegment_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_LinetypeSegment > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_LinetypeSegment *', 
                   [])
    cls.add_method('First', 
                   'ON_LinetypeSegment const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_LinetypeSegment *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_LinetypeSegment *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_LinetypeSegment *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_LinetypeSegment *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_LinetypeSegment const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_LinetypeSegment const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_LinetypeSegment const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_LinetypeSegment const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_LinetypeSegment *', 
                   [])
    cls.add_method('Last', 
                   'ON_LinetypeSegment const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_LinetypeSegment &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_LinetypeSegment const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_LinetypeSegment const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_LinetypeSegment const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_LinetypeSegment const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_LinetypeSegment const *', 'key'), param('int ( * ) ( ON_LinetypeSegment const *, ON_LinetypeSegment const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_LinetypeSegment const *', 'key'), param('int ( * ) ( ON_LinetypeSegment const *, ON_LinetypeSegment const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_LinetypeSegment const *', 'arg0'), param('int ( * ) ( ON_LinetypeSegment const *, ON_LinetypeSegment const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_LinetypeSegment const *, ON_LinetypeSegment const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_LinetypeSegment const *, ON_LinetypeSegment const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_LinetypeSegment const *, ON_LinetypeSegment const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_LinetypeSegment const *, ON_LinetypeSegment const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_LinetypeSegment *', 
                   [param('ON_LinetypeSegment *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_LinetypeSegment *', 
                   [])
    cls.add_method('Array', 
                   'ON_LinetypeSegment const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_LinetypeSegment *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_LinetypeSegment *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_LinetypeSegment *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_MappingChannel_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_MappingChannel > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MappingChannel *', 
                   [])
    cls.add_method('First', 
                   'ON_MappingChannel const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingChannel *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MappingChannel *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MappingChannel *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MappingChannel *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MappingChannel const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingChannel const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingChannel const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MappingChannel const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MappingChannel *', 
                   [])
    cls.add_method('Last', 
                   'ON_MappingChannel const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MappingChannel &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MappingChannel const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MappingChannel const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MappingChannel const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MappingChannel const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MappingChannel const *', 'key'), param('int ( * ) ( ON_MappingChannel const *, ON_MappingChannel const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MappingChannel const *', 'key'), param('int ( * ) ( ON_MappingChannel const *, ON_MappingChannel const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MappingChannel const *', 'arg0'), param('int ( * ) ( ON_MappingChannel const *, ON_MappingChannel const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MappingChannel const *, ON_MappingChannel const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MappingChannel const *, ON_MappingChannel const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MappingChannel const *, ON_MappingChannel const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MappingChannel const *, ON_MappingChannel const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MappingChannel *', 
                   [param('ON_MappingChannel *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MappingChannel *', 
                   [])
    cls.add_method('Array', 
                   'ON_MappingChannel const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MappingChannel *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MappingChannel *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MappingChannel *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_MeshFace_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_MeshFace > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MeshFace *', 
                   [])
    cls.add_method('First', 
                   'ON_MeshFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshFace *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MeshFace *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MeshFace *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshFace *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshFace const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshFace const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshFace const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshFace const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MeshFace *', 
                   [])
    cls.add_method('Last', 
                   'ON_MeshFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MeshFace &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MeshFace const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MeshFace const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MeshFace const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshFace const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshFace const *', 'key'), param('int ( * ) ( ON_MeshFace const *, ON_MeshFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshFace const *', 'key'), param('int ( * ) ( ON_MeshFace const *, ON_MeshFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshFace const *', 'arg0'), param('int ( * ) ( ON_MeshFace const *, ON_MeshFace const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshFace const *, ON_MeshFace const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshFace const *, ON_MeshFace const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshFace const *, ON_MeshFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshFace const *, ON_MeshFace const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MeshFace *', 
                   [param('ON_MeshFace *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MeshFace *', 
                   [])
    cls.add_method('Array', 
                   'ON_MeshFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MeshFace *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshFace *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshFace *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_MeshPart_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_MeshPart > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MeshPart *', 
                   [])
    cls.add_method('First', 
                   'ON_MeshPart const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshPart *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MeshPart *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MeshPart *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshPart *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshPart const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshPart const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshPart const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshPart const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MeshPart *', 
                   [])
    cls.add_method('Last', 
                   'ON_MeshPart const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MeshPart &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MeshPart const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MeshPart const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MeshPart const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshPart const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshPart const *', 'key'), param('int ( * ) ( ON_MeshPart const *, ON_MeshPart const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshPart const *', 'key'), param('int ( * ) ( ON_MeshPart const *, ON_MeshPart const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshPart const *', 'arg0'), param('int ( * ) ( ON_MeshPart const *, ON_MeshPart const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshPart const *, ON_MeshPart const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshPart const *, ON_MeshPart const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshPart const *, ON_MeshPart const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshPart const *, ON_MeshPart const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MeshPart *', 
                   [param('ON_MeshPart *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MeshPart *', 
                   [])
    cls.add_method('Array', 
                   'ON_MeshPart const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MeshPart *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshPart *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshPart *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_MeshTopologyEdge_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_MeshTopologyEdge > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MeshTopologyEdge *', 
                   [])
    cls.add_method('First', 
                   'ON_MeshTopologyEdge const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyEdge *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyEdge *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyEdge *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyEdge *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyEdge const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyEdge const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyEdge const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyEdge const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MeshTopologyEdge *', 
                   [])
    cls.add_method('Last', 
                   'ON_MeshTopologyEdge const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MeshTopologyEdge &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MeshTopologyEdge const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MeshTopologyEdge const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MeshTopologyEdge const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshTopologyEdge const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshTopologyEdge const *', 'key'), param('int ( * ) ( ON_MeshTopologyEdge const *, ON_MeshTopologyEdge const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshTopologyEdge const *', 'key'), param('int ( * ) ( ON_MeshTopologyEdge const *, ON_MeshTopologyEdge const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshTopologyEdge const *', 'arg0'), param('int ( * ) ( ON_MeshTopologyEdge const *, ON_MeshTopologyEdge const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshTopologyEdge const *, ON_MeshTopologyEdge const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshTopologyEdge const *, ON_MeshTopologyEdge const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshTopologyEdge const *, ON_MeshTopologyEdge const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshTopologyEdge const *, ON_MeshTopologyEdge const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MeshTopologyEdge *', 
                   [param('ON_MeshTopologyEdge *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MeshTopologyEdge *', 
                   [])
    cls.add_method('Array', 
                   'ON_MeshTopologyEdge const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MeshTopologyEdge *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshTopologyEdge *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshTopologyEdge *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_MeshTopologyFace_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_MeshTopologyFace > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MeshTopologyFace *', 
                   [])
    cls.add_method('First', 
                   'ON_MeshTopologyFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyFace *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyFace *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyFace *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyFace *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyFace const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyFace const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyFace const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyFace const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MeshTopologyFace *', 
                   [])
    cls.add_method('Last', 
                   'ON_MeshTopologyFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MeshTopologyFace &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MeshTopologyFace const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MeshTopologyFace const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MeshTopologyFace const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshTopologyFace const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshTopologyFace const *', 'key'), param('int ( * ) ( ON_MeshTopologyFace const *, ON_MeshTopologyFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshTopologyFace const *', 'key'), param('int ( * ) ( ON_MeshTopologyFace const *, ON_MeshTopologyFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshTopologyFace const *', 'arg0'), param('int ( * ) ( ON_MeshTopologyFace const *, ON_MeshTopologyFace const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshTopologyFace const *, ON_MeshTopologyFace const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshTopologyFace const *, ON_MeshTopologyFace const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshTopologyFace const *, ON_MeshTopologyFace const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshTopologyFace const *, ON_MeshTopologyFace const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MeshTopologyFace *', 
                   [param('ON_MeshTopologyFace *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MeshTopologyFace *', 
                   [])
    cls.add_method('Array', 
                   'ON_MeshTopologyFace const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MeshTopologyFace *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshTopologyFace *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshTopologyFace *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_MeshTopologyVertex_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_MeshTopologyVertex > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_MeshTopologyVertex *', 
                   [])
    cls.add_method('First', 
                   'ON_MeshTopologyVertex const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyVertex *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyVertex *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyVertex *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyVertex *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_MeshTopologyVertex const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyVertex const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyVertex const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_MeshTopologyVertex const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_MeshTopologyVertex *', 
                   [])
    cls.add_method('Last', 
                   'ON_MeshTopologyVertex const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_MeshTopologyVertex &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_MeshTopologyVertex const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_MeshTopologyVertex const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_MeshTopologyVertex const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshTopologyVertex const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_MeshTopologyVertex const *', 'key'), param('int ( * ) ( ON_MeshTopologyVertex const *, ON_MeshTopologyVertex const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshTopologyVertex const *', 'key'), param('int ( * ) ( ON_MeshTopologyVertex const *, ON_MeshTopologyVertex const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_MeshTopologyVertex const *', 'arg0'), param('int ( * ) ( ON_MeshTopologyVertex const *, ON_MeshTopologyVertex const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshTopologyVertex const *, ON_MeshTopologyVertex const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_MeshTopologyVertex const *, ON_MeshTopologyVertex const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshTopologyVertex const *, ON_MeshTopologyVertex const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_MeshTopologyVertex const *, ON_MeshTopologyVertex const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_MeshTopologyVertex *', 
                   [param('ON_MeshTopologyVertex *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_MeshTopologyVertex *', 
                   [])
    cls.add_method('Array', 
                   'ON_MeshTopologyVertex const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_MeshTopologyVertex *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshTopologyVertex *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_MeshTopologyVertex *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_ObjRef_IRefID_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_ObjRef_IRefID > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_ObjRef_IRefID *', 
                   [])
    cls.add_method('First', 
                   'ON_ObjRef_IRefID const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ObjRef_IRefID *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_ObjRef_IRefID *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_ObjRef_IRefID *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_ObjRef_IRefID *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_ObjRef_IRefID const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ObjRef_IRefID const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ObjRef_IRefID const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_ObjRef_IRefID const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_ObjRef_IRefID *', 
                   [])
    cls.add_method('Last', 
                   'ON_ObjRef_IRefID const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_ObjRef_IRefID &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_ObjRef_IRefID const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_ObjRef_IRefID const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_ObjRef_IRefID const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_ObjRef_IRefID const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_ObjRef_IRefID const *', 'key'), param('int ( * ) ( ON_ObjRef_IRefID const *, ON_ObjRef_IRefID const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_ObjRef_IRefID const *', 'key'), param('int ( * ) ( ON_ObjRef_IRefID const *, ON_ObjRef_IRefID const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_ObjRef_IRefID const *', 'arg0'), param('int ( * ) ( ON_ObjRef_IRefID const *, ON_ObjRef_IRefID const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_ObjRef_IRefID const *, ON_ObjRef_IRefID const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_ObjRef_IRefID const *, ON_ObjRef_IRefID const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_ObjRef_IRefID const *, ON_ObjRef_IRefID const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_ObjRef_IRefID const *, ON_ObjRef_IRefID const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_ObjRef_IRefID *', 
                   [param('ON_ObjRef_IRefID *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_ObjRef_IRefID *', 
                   [])
    cls.add_method('Array', 
                   'ON_ObjRef_IRefID const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_ObjRef_IRefID *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_ObjRef_IRefID *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_ObjRef_IRefID *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_OffsetSurfaceValue_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_OffsetSurfaceValue > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_OffsetSurfaceValue *', 
                   [])
    cls.add_method('First', 
                   'ON_OffsetSurfaceValue const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_OffsetSurfaceValue const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_OffsetSurfaceValue *', 
                   [])
    cls.add_method('Last', 
                   'ON_OffsetSurfaceValue const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_OffsetSurfaceValue &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_OffsetSurfaceValue const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_OffsetSurfaceValue const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_OffsetSurfaceValue const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_OffsetSurfaceValue const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_OffsetSurfaceValue const *', 'key'), param('int ( * ) ( ON_OffsetSurfaceValue const *, ON_OffsetSurfaceValue const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_OffsetSurfaceValue const *', 'key'), param('int ( * ) ( ON_OffsetSurfaceValue const *, ON_OffsetSurfaceValue const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_OffsetSurfaceValue const *', 'arg0'), param('int ( * ) ( ON_OffsetSurfaceValue const *, ON_OffsetSurfaceValue const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_OffsetSurfaceValue const *, ON_OffsetSurfaceValue const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_OffsetSurfaceValue const *, ON_OffsetSurfaceValue const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_OffsetSurfaceValue const *, ON_OffsetSurfaceValue const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_OffsetSurfaceValue const *, ON_OffsetSurfaceValue const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_OffsetSurfaceValue *', 
                   [param('ON_OffsetSurfaceValue *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_OffsetSurfaceValue *', 
                   [])
    cls.add_method('Array', 
                   'ON_OffsetSurfaceValue const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_OffsetSurfaceValue *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_OffsetSurfaceValue *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_OffsetSurfaceValue *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_Surface__star___methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_Surface * > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Surface * *', 
                   [])
    cls.add_method('First', 
                   'ON_Surface * const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Surface * *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Surface * *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Surface * *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Surface * *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Surface * const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Surface * const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Surface * const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Surface * const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Surface * *', 
                   [])
    cls.add_method('Last', 
                   'ON_Surface * const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Surface * &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Surface * const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Surface * const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Surface * const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Surface * const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Surface * const *', 'key'), param('int ( * ) ( ON_Surface * const *, ON_Surface * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Surface * const *', 'key'), param('int ( * ) ( ON_Surface * const *, ON_Surface * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Surface * const *', 'arg0'), param('int ( * ) ( ON_Surface * const *, ON_Surface * const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Surface * const *, ON_Surface * const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Surface * const *, ON_Surface * const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Surface * const *, ON_Surface * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Surface * const *, ON_Surface * const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Surface * *', 
                   [param('ON_Surface * *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Surface * *', 
                   [])
    cls.add_method('Array', 
                   'ON_Surface * const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Surface * *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Surface * *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Surface * *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_SurfaceCurvature_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_SurfaceCurvature > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_SurfaceCurvature *', 
                   [])
    cls.add_method('First', 
                   'ON_SurfaceCurvature const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_SurfaceCurvature *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_SurfaceCurvature *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_SurfaceCurvature *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_SurfaceCurvature *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_SurfaceCurvature const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_SurfaceCurvature const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_SurfaceCurvature const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_SurfaceCurvature const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_SurfaceCurvature *', 
                   [])
    cls.add_method('Last', 
                   'ON_SurfaceCurvature const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_SurfaceCurvature &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_SurfaceCurvature const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_SurfaceCurvature const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_SurfaceCurvature const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_SurfaceCurvature const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_SurfaceCurvature const *', 'key'), param('int ( * ) ( ON_SurfaceCurvature const *, ON_SurfaceCurvature const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_SurfaceCurvature const *', 'key'), param('int ( * ) ( ON_SurfaceCurvature const *, ON_SurfaceCurvature const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_SurfaceCurvature const *', 'arg0'), param('int ( * ) ( ON_SurfaceCurvature const *, ON_SurfaceCurvature const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_SurfaceCurvature const *, ON_SurfaceCurvature const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_SurfaceCurvature const *, ON_SurfaceCurvature const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_SurfaceCurvature const *, ON_SurfaceCurvature const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_SurfaceCurvature const *, ON_SurfaceCurvature const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_SurfaceCurvature *', 
                   [param('ON_SurfaceCurvature *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_SurfaceCurvature *', 
                   [])
    cls.add_method('Array', 
                   'ON_SurfaceCurvature const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_SurfaceCurvature *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_SurfaceCurvature *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_SurfaceCurvature *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_UUID_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_UUID > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_UUID const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_UUID const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_UUID &', 
                   [])
    cls.add_method('Array', 
                   'ON_UUID *', 
                   [])
    cls.add_method('Array', 
                   'ON_UUID const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UUID *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_UUID *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_UUID *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_UUID *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_UUID const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UUID const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UUID const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UUID const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UUID const *', 'arg0'), param('int ( * ) ( ON_UUID const *, ON_UUID const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UUID const *', 'arg0'), param('int ( * ) ( ON_UUID const *, ON_UUID const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_UUID *', 
                   [])
    cls.add_method('First', 
                   'ON_UUID const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UUID const *, ON_UUID const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_UUID const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_UUID *', 
                   [])
    cls.add_method('Last', 
                   'ON_UUID *', 
                   [])
    cls.add_method('Last', 
                   'ON_UUID const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UUID const *, ON_UUID const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_UUID *', 
                   [param('ON_UUID *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_UUID const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_UUID const *', 'arg0'), param('int ( * ) ( ON_UUID const *, ON_UUID const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UUID *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UUID *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_UUID const *, ON_UUID const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_UUID const *, ON_UUID const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_UuidIndex_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_UuidIndex > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_UuidIndex const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_UuidIndex const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_UuidIndex &', 
                   [])
    cls.add_method('Array', 
                   'ON_UuidIndex *', 
                   [])
    cls.add_method('Array', 
                   'ON_UuidIndex const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidIndex *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidIndex *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidIndex *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidIndex *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidIndex const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidIndex const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidIndex const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidIndex const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UuidIndex const *', 'arg0'), param('int ( * ) ( ON_UuidIndex const *, ON_UuidIndex const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UuidIndex const *', 'arg0'), param('int ( * ) ( ON_UuidIndex const *, ON_UuidIndex const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_UuidIndex *', 
                   [])
    cls.add_method('First', 
                   'ON_UuidIndex const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UuidIndex const *, ON_UuidIndex const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_UuidIndex const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_UuidIndex *', 
                   [])
    cls.add_method('Last', 
                   'ON_UuidIndex *', 
                   [])
    cls.add_method('Last', 
                   'ON_UuidIndex const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UuidIndex const *, ON_UuidIndex const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_UuidIndex *', 
                   [param('ON_UuidIndex *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_UuidIndex const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_UuidIndex const *', 'arg0'), param('int ( * ) ( ON_UuidIndex const *, ON_UuidIndex const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UuidIndex *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UuidIndex *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_UuidIndex const *, ON_UuidIndex const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_UuidIndex const *, ON_UuidIndex const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_UuidPair_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< ON_UuidPair > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_UuidPair const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('ON_UuidPair const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'ON_UuidPair &', 
                   [])
    cls.add_method('Array', 
                   'ON_UuidPair *', 
                   [])
    cls.add_method('Array', 
                   'ON_UuidPair const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidPair *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidPair *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidPair *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidPair *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'ON_UuidPair const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidPair const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidPair const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_UuidPair const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UuidPair const *', 'arg0'), param('int ( * ) ( ON_UuidPair const *, ON_UuidPair const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_UuidPair const *', 'arg0'), param('int ( * ) ( ON_UuidPair const *, ON_UuidPair const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'ON_UuidPair *', 
                   [])
    cls.add_method('First', 
                   'ON_UuidPair const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UuidPair const *, ON_UuidPair const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('ON_UuidPair const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'ON_UuidPair *', 
                   [])
    cls.add_method('Last', 
                   'ON_UuidPair *', 
                   [])
    cls.add_method('Last', 
                   'ON_UuidPair const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_UuidPair const *, ON_UuidPair const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'ON_UuidPair *', 
                   [param('ON_UuidPair *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_UuidPair const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_UuidPair const *', 'arg0'), param('int ( * ) ( ON_UuidPair const *, ON_UuidPair const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UuidPair *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_UuidPair *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_UuidPair const *, ON_UuidPair const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( ON_UuidPair const *, ON_UuidPair const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__ON_Value__star___methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< ON_Value * > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'ON_Value * *', 
                   [])
    cls.add_method('First', 
                   'ON_Value * const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Value * *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'ON_Value * *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'ON_Value * *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'ON_Value * *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'ON_Value * const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Value * const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Value * const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'ON_Value * const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'ON_Value * *', 
                   [])
    cls.add_method('Last', 
                   'ON_Value * const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'ON_Value * &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('ON_Value * const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('ON_Value * const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('ON_Value * const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Value * const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('ON_Value * const *', 'key'), param('int ( * ) ( ON_Value * const *, ON_Value * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Value * const *', 'key'), param('int ( * ) ( ON_Value * const *, ON_Value * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('ON_Value * const *', 'arg0'), param('int ( * ) ( ON_Value * const *, ON_Value * const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Value * const *, ON_Value * const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( ON_Value * const *, ON_Value * const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Value * const *, ON_Value * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( ON_Value * const *, ON_Value * const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'ON_Value * *', 
                   [param('ON_Value * *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'ON_Value * *', 
                   [])
    cls.add_method('Array', 
                   'ON_Value * const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'ON_Value * *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Value * *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('ON_Value * *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__Bool_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< bool > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'bool *', 
                   [])
    cls.add_method('First', 
                   'bool const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'bool *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'bool *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'bool *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'bool *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'bool const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'bool const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'bool const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'bool const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'bool *', 
                   [])
    cls.add_method('Last', 
                   'bool const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'bool &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('bool const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('bool const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('bool const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('bool const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('bool const *', 'key'), param('int ( * ) ( bool const *, bool const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('bool const *', 'key'), param('int ( * ) ( bool const *, bool const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('bool const *', 'arg0'), param('int ( * ) ( bool const *, bool const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( bool const *, bool const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( bool const *, bool const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( bool const *, bool const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( bool const *, bool const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'bool *', 
                   [param('bool *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'bool *', 
                   [])
    cls.add_method('Array', 
                   'bool const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'bool *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('bool *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('bool *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__Double__star___methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< double * > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'double * *', 
                   [])
    cls.add_method('First', 
                   'double * const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'double * *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'double * *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'double * *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'double * *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'double * const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'double * const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'double * const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'double * const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'double * *', 
                   [])
    cls.add_method('Last', 
                   'double * const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'double * &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('double * const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('double * const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('double * const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('double * const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('double * const *', 'key'), param('int ( * ) ( double * const *, double * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('double * const *', 'key'), param('int ( * ) ( double * const *, double * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('double * const *', 'arg0'), param('int ( * ) ( double * const *, double * const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( double * const *, double * const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( double * const *, double * const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( double * const *, double * const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( double * const *, double * const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'double * *', 
                   [param('double * *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'double * *', 
                   [])
    cls.add_method('Array', 
                   'double * const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'double * *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('double * *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('double * *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__Double_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< double > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'double *', 
                   [])
    cls.add_method('First', 
                   'double const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'double *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'double *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'double *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'double *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'double const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'double const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'double const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'double const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'double *', 
                   [])
    cls.add_method('Last', 
                   'double const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'double &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('double const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('double const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('double const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('double const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('double const *', 'key'), param('int ( * ) ( double const *, double const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('double const *', 'key'), param('int ( * ) ( double const *, double const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('double const *', 'arg0'), param('int ( * ) ( double const *, double const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( double const *, double const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( double const *, double const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( double const *, double const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( double const *, double const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'double *', 
                   [param('double *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'double *', 
                   [])
    cls.add_method('Array', 
                   'double const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'double *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('double *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('double *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__Int_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'c')])
    cls.add_constructor([param('ON_SimpleArray< int > const &', 'src')])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('First', 
                   'int *', 
                   [])
    cls.add_method('First', 
                   'int const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'int *', 
                   [param('int', 'i')])
    cls.add_method('At', 
                   'int *', 
                   [param('unsigned int', 'i')])
    cls.add_method('At', 
                   'int *', 
                   [param('ON__INT64', 'i')])
    cls.add_method('At', 
                   'int *', 
                   [param('ON__UINT64', 'i')])
    cls.add_method('At', 
                   'int const *', 
                   [param('int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'int const *', 
                   [param('unsigned int', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'int const *', 
                   [param('ON__INT64', 'i')], 
                   is_const=True)
    cls.add_method('At', 
                   'int const *', 
                   [param('ON__UINT64', 'i')], 
                   is_const=True)
    cls.add_method('Last', 
                   'int *', 
                   [])
    cls.add_method('Last', 
                   'int const *', 
                   [], 
                   is_const=True)
    cls.add_method('AppendNew', 
                   'int &', 
                   [])
    cls.add_method('Append', 
                   'void', 
                   [param('int const &', 'x')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'count'), param('int const *', 'p')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'i'), param('int const &', 'x')])
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'i')], 
                   is_virtual=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('Search', 
                   'int', 
                   [param('int const &', 'key')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('int const *', 'key'), param('int ( * ) ( int const *, int const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('int const *', 'key'), param('int ( * ) ( int const *, int const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('int const *', 'arg0'), param('int ( * ) ( int const *, int const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( int const *, int const * ) *', 'compar')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( int const *, int const * ) *', 'compar')])
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( int const *, int const * ) *', 'compar')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sa'), param('int *', 'index'), param('int ( * ) ( int const *, int const *, void * ) *', 'compar'), param('void *', 'p')], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'index')])
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'value')])
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'newcap')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Realloc', 
                   'int *', 
                   [param('int *', 'ptr'), param('int', 'capacity')], 
                   is_virtual=True)
    cls.add_method('Array', 
                   'int *', 
                   [])
    cls.add_method('Array', 
                   'int const *', 
                   [], 
                   is_const=True)
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'count')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'capacity')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('KeepArray', 
                   'int *', 
                   [])
    cls.add_method('SetArray', 
                   'void', 
                   [param('int *', 'p')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('int *', 'p'), param('int', 'count'), param('int', 'capacity')])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'dest_i'), param('int', 'src_i'), param('int', 'ele_cnt')], 
                   visibility='protected')
    return

def register_ON_SimpleArray__TagON_2dex_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'arg0')])
    cls.add_constructor([param('ON_SimpleArray< tagON_2dex > const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('tagON_2dex const &', 'arg0')])
    cls.add_method('Append', 
                   'void', 
                   [param('int', 'arg0'), param('tagON_2dex const *', 'arg1')])
    cls.add_method('AppendNew', 
                   'tagON_2dex &', 
                   [])
    cls.add_method('Array', 
                   'tagON_2dex *', 
                   [])
    cls.add_method('Array', 
                   'tagON_2dex const *', 
                   [], 
                   is_const=True)
    cls.add_method('At', 
                   'tagON_2dex *', 
                   [param('int', 'arg0')])
    cls.add_method('At', 
                   'tagON_2dex *', 
                   [param('unsigned int', 'arg0')])
    cls.add_method('At', 
                   'tagON_2dex *', 
                   [param('ON__INT64', 'arg0')])
    cls.add_method('At', 
                   'tagON_2dex *', 
                   [param('ON__UINT64', 'arg0')])
    cls.add_method('At', 
                   'tagON_2dex const *', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'tagON_2dex const *', 
                   [param('unsigned int', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'tagON_2dex const *', 
                   [param('ON__INT64', 'arg0')], 
                   is_const=True)
    cls.add_method('At', 
                   'tagON_2dex const *', 
                   [param('ON__UINT64', 'arg0')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('tagON_2dex const *', 'arg0'), param('int ( * ) ( tagON_2dex const *, tagON_2dex const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('BinarySearch', 
                   'int', 
                   [param('tagON_2dex const *', 'arg0'), param('int ( * ) ( tagON_2dex const *, tagON_2dex const * ) *', 'arg1'), param('int', 'arg2')], 
                   is_const=True)
    cls.add_method('Capacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('First', 
                   'tagON_2dex *', 
                   [])
    cls.add_method('First', 
                   'tagON_2dex const *', 
                   [], 
                   is_const=True)
    cls.add_method('HeapSort', 
                   'bool', 
                   [param('int ( * ) ( tagON_2dex const *, tagON_2dex const * ) *', 'arg0')])
    cls.add_method('Insert', 
                   'void', 
                   [param('int', 'arg0'), param('tagON_2dex const &', 'arg1')])
    cls.add_method('KeepArray', 
                   'tagON_2dex *', 
                   [])
    cls.add_method('Last', 
                   'tagON_2dex *', 
                   [])
    cls.add_method('Last', 
                   'tagON_2dex const *', 
                   [], 
                   is_const=True)
    cls.add_method('MemSet', 
                   'void', 
                   [param('unsigned char', 'arg0')])
    cls.add_method('NewCapacity', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Permute', 
                   'bool', 
                   [param('int const *', 'arg0')])
    cls.add_method('QuickSort', 
                   'bool', 
                   [param('int ( * ) ( tagON_2dex const *, tagON_2dex const * ) *', 'arg0')])
    cls.add_method('Realloc', 
                   'tagON_2dex *', 
                   [param('tagON_2dex *', 'arg0'), param('int', 'arg1')], 
                   is_virtual=True)
    cls.add_method('Remove', 
                   'void', 
                   [])
    cls.add_method('Remove', 
                   'void', 
                   [param('int', 'arg0')], 
                   is_virtual=True)
    cls.add_method('Reserve', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Reverse', 
                   'void', 
                   [])
    cls.add_method('Search', 
                   'int', 
                   [param('tagON_2dex const &', 'arg0')], 
                   is_const=True)
    cls.add_method('Search', 
                   'int', 
                   [param('tagON_2dex const *', 'arg0'), param('int ( * ) ( tagON_2dex const *, tagON_2dex const * ) *', 'arg1')], 
                   is_const=True)
    cls.add_method('SetArray', 
                   'void', 
                   [param('tagON_2dex *', 'arg0')])
    cls.add_method('SetArray', 
                   'void', 
                   [param('tagON_2dex *', 'arg0'), param('int', 'arg1'), param('int', 'arg2')])
    cls.add_method('SetCapacity', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('SetCount', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('Shrink', 
                   'void', 
                   [])
    cls.add_method('SizeOfArray', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOfElement', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( tagON_2dex const *, tagON_2dex const * ) *', 'arg2')], 
                   is_const=True)
    cls.add_method('Sort', 
                   'bool', 
                   [param('ON::sort_algorithm', 'sort_algorithm'), param('int *', 'arg1'), param('int ( * ) ( tagON_2dex const *, tagON_2dex const *, void * ) *', 'arg2'), param('void *', 'arg3')], 
                   is_const=True)
    cls.add_method('Swap', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1')])
    cls.add_method('UnsignedCount', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('Zero', 
                   'void', 
                   [])
    cls.add_method('Move', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('int', 'arg2')], 
                   visibility='protected')
    return

def register_ON_SpaceMorph_methods(root_module, cls):
    cls.add_constructor([param('ON_SpaceMorph const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('IsIdentity', 
                   'bool', 
                   [param('ON_BoundingBox const &', 'bbox')], 
                   is_const=True, is_virtual=True)
    cls.add_method('PreserveStructure', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('QuickPreview', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('SetPreserveStructure', 
                   'void', 
                   [param('bool', 'bPreserveStructure')])
    cls.add_method('SetQuickPreview', 
                   'void', 
                   [param('bool', 'bQuickPreview')])
    cls.add_method('SetTolerance', 
                   'void', 
                   [param('double', 'tolerance')])
    cls.add_method('Tolerance', 
                   'double', 
                   [], 
                   is_const=True)
    return

def register_ON_Sphere_methods(root_module, cls):
    cls.add_constructor([param('ON_Sphere const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_3dPoint const &', 'center'), param('double', 'radius')])
    cls.add_method('BoundingBox', 
                   'ON_BoundingBox', 
                   [], 
                   is_const=True)
    cls.add_method('Center', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'bool', 
                   [param('ON_3dPoint', 'test_point'), param('double *', 'longitude_radians'), param('double *', 'latitude_radians')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'test_point')], 
                   is_const=True)
    cls.add_method('Create', 
                   'bool', 
                   [param('ON_3dPoint const &', 'center'), param('double', 'radius')])
    cls.add_method('Diameter', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('GetNurbForm', 
                   'int', 
                   [param('ON_NurbsSurface &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('LatitudeDegrees', 
                   'ON_Circle', 
                   [param('double', 'latitude_degrees')], 
                   is_const=True)
    cls.add_method('LatitudeRadians', 
                   'ON_Circle', 
                   [param('double', 'latitude_radians')], 
                   is_const=True)
    cls.add_method('LongitudeDegrees', 
                   'ON_Circle', 
                   [param('double', 'longitude_degrees')], 
                   is_const=True)
    cls.add_method('LongitudeRadians', 
                   'ON_Circle', 
                   [param('double', 'longitude_radians')], 
                   is_const=True)
    cls.add_method('NormalAt', 
                   'ON_3dVector', 
                   [param('double', 'longitude_radians'), param('double', 'latitude_radians')], 
                   is_const=True)
    cls.add_method('NorthPole', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'longitude_radians'), param('double', 'latitude_radians')], 
                   is_const=True)
    cls.add_method('Radius', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('RevSurfaceForm', 
                   'ON_RevSurface *', 
                   [param('bool', 'bArcLengthParameterization'), param('ON_RevSurface *', 'srf', default_value='0')], 
                   is_const=True)
    cls.add_method('RevSurfaceForm', 
                   'ON_RevSurface *', 
                   [param('ON_RevSurface *', 'srf', default_value='0')], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle_radians'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Rotate', 
                   'bool', 
                   [param('double', 'angle_radians'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('SouthPole', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('Transform', 
                   'bool', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Translate', 
                   'bool', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_instance_attribute('plane', 'ON_Plane', is_const=False)
    cls.add_instance_attribute('radius', 'double', is_const=False)
    return

def register_ON_String_methods(root_module, cls):
    cls.add_binary_numeric_operator('+', root_module['ON_String'], root_module['ON_String'], param('ON_String const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_String'], root_module['ON_String'], param('char', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_String'], root_module['ON_String'], param('unsigned char', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_String'], root_module['ON_String'], param('char const *', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ON_String'], root_module['ON_String'], param('unsigned char const *', u'right'))
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('>=')
    cls.add_inplace_numeric_operator('+=', param('ON_String const &', u'right'))
    cls.add_inplace_numeric_operator('+=', param('char', u'right'))
    cls.add_inplace_numeric_operator('+=', param('unsigned char', u'right'))
    cls.add_inplace_numeric_operator('+=', param('char const *', u'right'))
    cls.add_inplace_numeric_operator('+=', param('unsigned char const *', u'right'))
    cls.add_constructor([])
    cls.add_constructor([param('ON_String const &', 'arg0')])
    cls.add_constructor([param('char const *', 'arg0')])
    cls.add_constructor([param('char const *', 'arg0'), param('int', 'arg1')])
    cls.add_constructor([param('char', 'arg0'), param('int', 'arg1', default_value='1')])
    cls.add_constructor([param('unsigned char const *', 'arg0')])
    cls.add_constructor([param('unsigned char const *', 'arg0'), param('int', 'arg1')])
    cls.add_constructor([param('unsigned char', 'arg0'), param('int', 'arg1', default_value='1')])
    cls.add_constructor([param('wchar_t const *', 'src')])
    cls.add_constructor([param('wchar_t const *', 'src'), param('int', 'length')])
    cls.add_constructor([param('ON_wString const &', 'src')])
    cls.add_method('Append', 
                   'void', 
                   [param('char const *', 'arg0'), param('int', 'arg1')])
    cls.add_method('Append', 
                   'void', 
                   [param('unsigned char const *', 'arg0'), param('int', 'arg1')])
    cls.add_method('Array', 
                   'char *', 
                   [])
    cls.add_method('Array', 
                   'char const *', 
                   [], 
                   is_const=True)
    cls.add_method('Compare', 
                   'int', 
                   [param('char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('Compare', 
                   'int', 
                   [param('unsigned char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('CompareNoCase', 
                   'int', 
                   [param('char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('CompareNoCase', 
                   'int', 
                   [param('unsigned char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('Create', 
                   'void', 
                   [])
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True)
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('EmergencyDestroy', 
                   'void', 
                   [])
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('EnableReferenceCounting', 
                   'void', 
                   [param('bool', 'bEnable')])
    cls.add_method('Find', 
                   'int', 
                   [param('char', 'arg0')], 
                   is_const=True)
    cls.add_method('Find', 
                   'int', 
                   [param('unsigned char', 'arg0')], 
                   is_const=True)
    cls.add_method('Find', 
                   'int', 
                   [param('char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('Find', 
                   'int', 
                   [param('unsigned char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('Format', 
                   'void', 
                   [param('char const *', 'arg0'), param('. . .', '')])
    cls.add_method('Format', 
                   'void', 
                   [param('unsigned char const *', 'arg0'), param('. . .', '')])
    cls.add_method('GetAt', 
                   'char', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('IsEmpty', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsReferenceCounted', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Left', 
                   'ON_String', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('Length', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('MakeLower', 
                   'void', 
                   [])
    cls.add_method('MakeReverse', 
                   'void', 
                   [])
    cls.add_method('MakeUpper', 
                   'void', 
                   [])
    cls.add_method('Mid', 
                   'ON_String', 
                   [param('int', 'arg0'), param('int', 'arg1')], 
                   is_const=True)
    cls.add_method('Mid', 
                   'ON_String', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('Remove', 
                   'int', 
                   [param('char const', 'chRemove')])
    cls.add_method('Replace', 
                   'int', 
                   [param('char const *', 'token1'), param('char const *', 'token2')])
    cls.add_method('Replace', 
                   'int', 
                   [param('unsigned char const *', 'token1'), param('unsigned char const *', 'token2')])
    cls.add_method('Replace', 
                   'int', 
                   [param('char', 'token1'), param('char', 'token2')])
    cls.add_method('Replace', 
                   'int', 
                   [param('unsigned char', 'token1'), param('unsigned char', 'token2')])
    cls.add_method('ReserveArray', 
                   'void', 
                   [param('size_t', 'arg0')])
    cls.add_method('ReverseFind', 
                   'int', 
                   [param('char', 'arg0')], 
                   is_const=True)
    cls.add_method('ReverseFind', 
                   'int', 
                   [param('unsigned char', 'arg0')], 
                   is_const=True)
    cls.add_method('Right', 
                   'ON_String', 
                   [param('int', 'arg0')], 
                   is_const=True)
    cls.add_method('SetAt', 
                   'void', 
                   [param('int', 'arg0'), param('char', 'arg1')])
    cls.add_method('SetAt', 
                   'void', 
                   [param('int', 'arg0'), param('unsigned char', 'arg1')])
    cls.add_method('SetLength', 
                   'void', 
                   [param('size_t', 'arg0')])
    cls.add_method('ShrinkArray', 
                   'void', 
                   [])
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True)
    cls.add_method('SplitPath', 
                   'void', 
                   [param('char const *', 'path'), param('ON_String *', 'drive'), param('ON_String *', 'dir'), param('ON_String *', 'fname'), param('ON_String *', 'ext')], 
                   is_static=True)
    cls.add_method('TrimLeft', 
                   'void', 
                   [param('char const *', 'arg0', default_value='0')])
    cls.add_method('TrimLeftAndRight', 
                   'void', 
                   [param('char const *', 'arg0', default_value='0')])
    cls.add_method('TrimRight', 
                   'void', 
                   [param('char const *', 'arg0', default_value='0')])
    cls.add_method('WildCardMatch', 
                   'bool', 
                   [param('char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('WildCardMatch', 
                   'bool', 
                   [param('unsigned char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('WildCardMatchNoCase', 
                   'bool', 
                   [param('char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('WildCardMatchNoCase', 
                   'bool', 
                   [param('unsigned char const *', 'arg0')], 
                   is_const=True)
    cls.add_method('AppendToArray', 
                   'void', 
                   [param('ON_String const &', 'arg0')], 
                   visibility='protected')
    cls.add_method('AppendToArray', 
                   'void', 
                   [param('int', 'arg0'), param('char const *', 'arg1')], 
                   visibility='protected')
    cls.add_method('AppendToArray', 
                   'void', 
                   [param('int', 'arg0'), param('unsigned char const *', 'arg1')], 
                   visibility='protected')
    cls.add_method('CopyArray', 
                   'void', 
                   [], 
                   visibility='protected')
    cls.add_method('CopyToArray', 
                   'void', 
                   [param('ON_String const &', 'arg0')], 
                   visibility='protected')
    cls.add_method('CopyToArray', 
                   'void', 
                   [param('int', 'arg0'), param('char const *', 'arg1')], 
                   visibility='protected')
    cls.add_method('CopyToArray', 
                   'void', 
                   [param('int', 'arg0'), param('unsigned char const *', 'arg1')], 
                   visibility='protected')
    cls.add_method('CopyToArray', 
                   'void', 
                   [param('int', 'arg0'), param('wchar_t const *', 'arg1')], 
                   visibility='protected')
    cls.add_method('CreateArray', 
                   'void', 
                   [param('int', 'arg0')], 
                   visibility='protected')
    cls.add_method('Header', 
                   'ON_aStringHeader *', 
                   [], 
                   is_const=True, visibility='protected')
    cls.add_method('Length', 
                   'int', 
                   [param('char const *', 'arg0')], 
                   is_static=True, visibility='protected')
    cls.add_method('Length', 
                   'int', 
                   [param('unsigned char const *', 'arg0')], 
                   is_static=True, visibility='protected')
    return

def register_ON_Sum_methods(root_module, cls):
    cls.add_constructor([param('ON_Sum const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Begin', 
                   'void', 
                   [param('double', 'starting_value', default_value='0.0')])
    cls.add_method('Plus', 
                   'void', 
                   [param('double', 'x')])
    cls.add_method('SummandCount', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Total', 
                   'double', 
                   [param('double *', 'error_estimate', default_value='0')])
    return

def register_ON_SurfaceArray_methods(root_module, cls):
    cls.add_constructor([param('ON_SurfaceArray const &', 'arg0')])
    cls.add_constructor([param('int', 'arg0', default_value='0')])
    cls.add_method('Destroy', 
                   'void', 
                   [])
    cls.add_method('Duplicate', 
                   'ON_BOOL32', 
                   [param('ON_SurfaceArray &', 'arg0')], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    return

def register_ON_SurfaceCurvature_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_SurfaceCurvature const &', 'arg0')])
    cls.add_method('GaussianCurvature', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MaximumRadius', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MeanCurvature', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MinimumRadius', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_instance_attribute('k1', 'double', is_const=False)
    cls.add_instance_attribute('k2', 'double', is_const=False)
    return

def register_ON_SurfaceProperties_methods(root_module, cls):
    cls.add_constructor([param('ON_SurfaceProperties const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Set', 
                   'void', 
                   [param('ON_Surface const *', 'surface')])
    cls.add_instance_attribute('m_bHasSeam', 'bool', is_const=False)
    cls.add_instance_attribute('m_bHasSingularity', 'bool', is_const=False)
    cls.add_instance_attribute('m_bIsClosed', 'bool [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_bIsSet', 'bool', is_const=False)
    cls.add_instance_attribute('m_bIsSingular', 'bool [ 4 ]', is_const=False)
    cls.add_instance_attribute('m_domain', 'ON_Interval [ 2 ]', is_const=False)
    cls.add_instance_attribute('m_surface', 'ON_Surface const *', is_const=False)
    cls.add_instance_attribute('m_tag', 'ON__INT_PTR', is_const=False)
    return

def register_ON_TensorProduct_methods(root_module, cls):
    cls.add_constructor([param('ON_TensorProduct const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('DimensionA', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    cls.add_method('DimensionB', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    cls.add_method('DimensionC', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    cls.add_method('Evaluate', 
                   'bool', 
                   [param('double', 'arg0'), param('double const *', 'arg1'), param('double', 'arg2'), param('double const *', 'arg3'), param('double *', 'arg4')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_ON_TextLog_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('FILE *', 'fp')])
    cls.add_constructor([param('ON_wString &', 's')])
    cls.add_method('GetDoubleFormat', 
                   'void', 
                   [param('ON_String &', 'arg0')], 
                   is_const=True)
    cls.add_method('GetFloatFormat', 
                   'void', 
                   [param('ON_String &', 'arg0')], 
                   is_const=True)
    cls.add_method('IndentSize', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('PopIndent', 
                   'void', 
                   [])
    cls.add_method('Print', 
                   'void', 
                   [param('char const *', 'format'), param('. . .', '')])
    cls.add_method('Print', 
                   'void', 
                   [param('wchar_t const *', 'format'), param('. . .', '')])
    cls.add_method('Print', 
                   'void', 
                   [param('float', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('double', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_2dPoint const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_3dPoint const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_4dPoint const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_2dVector const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_UUID const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_COMPONENT_INDEX const &', 'arg0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_wString const &', 'string')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_String const &', 'string')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_3dPointArray const &', 'arg0'), param('char const *', 'arg1', default_value='0')])
    cls.add_method('Print', 
                   'void', 
                   [param('ON_Matrix const &', 'arg0'), param('char const *', 'arg1', default_value='0'), param('int', 'arg2', default_value='0')])
    cls.add_method('PrintKnotVector', 
                   'void', 
                   [param('int', 'arg0'), param('int', 'arg1'), param('double const *', 'arg2')])
    cls.add_method('PrintNewLine', 
                   'void', 
                   [])
    cls.add_method('PrintPointGrid', 
                   'void', 
                   [param('int', 'arg0'), param('ON_BOOL32', 'arg1'), param('int', 'arg2'), param('int', 'arg3'), param('int', 'arg4'), param('int', 'arg5'), param('double const *', 'arg6'), param('char const *', 'arg7', default_value='0')])
    cls.add_method('PrintPointList', 
                   'void', 
                   [param('int', 'arg0'), param('ON_BOOL32', 'arg1'), param('int', 'arg2'), param('int', 'arg3'), param('double const *', 'arg4'), param('char const *', 'arg5', default_value='0')])
    cls.add_method('PrintRGB', 
                   'void', 
                   [param('ON_Color const &', 'arg0')])
    cls.add_method('PrintString', 
                   'void', 
                   [param('char const *', 's')])
    cls.add_method('PrintString', 
                   'void', 
                   [param('wchar_t const *', 's')])
    cls.add_method('PrintTime', 
                   'void', 
                   [param('tm const &', 'arg0')])
    cls.add_method('PrintWrappedText', 
                   'void', 
                   [param('char const *', 'arg0'), param('int', 'arg1', default_value='60')])
    cls.add_method('PrintWrappedText', 
                   'void', 
                   [param('wchar_t const *', 'arg0'), param('int', 'arg1', default_value='60')])
    cls.add_method('PushIndent', 
                   'void', 
                   [])
    cls.add_method('SetDoubleFormat', 
                   'void', 
                   [param('char const *', 'arg0')])
    cls.add_method('SetFloatFormat', 
                   'void', 
                   [param('char const *', 'arg0')])
    cls.add_method('SetIndentSize', 
                   'void', 
                   [param('int', 'arg0')])
    cls.add_method('AppendText', 
                   'void', 
                   [param('char const *', 's')], 
                   visibility='protected', is_virtual=True)
    cls.add_method('AppendText', 
                   'void', 
                   [param('wchar_t const *', 's')], 
                   visibility='protected', is_virtual=True)
    return

def register_ON_Texture_methods(root_module, cls):
    cls.add_constructor([param('ON_Texture const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Cast', 
                   'ON_Texture *', 
                   [param('ON_Object *', 'arg0')], 
                   is_static=True)
    cls.add_method('Cast', 
                   'ON_Texture const *', 
                   [param('ON_Object const *', 'arg0')], 
                   is_static=True)
    cls.add_method('ClassId', 
                   'ON_ClassId const *', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Compare', 
                   'int', 
                   [param('ON_Texture const &', 'other')], 
                   is_const=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Duplicate', 
                   'ON_Texture *', 
                   [], 
                   is_const=True)
    cls.add_method('FilterFromInt', 
                   'ON_Texture::FILTER', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('IsTiled', 
                   'bool', 
                   [param('int', 'dir'), param('double *', 'count'), param('double *', 'offset')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True, is_virtual=True)
    cls.add_method('ModeFromInt', 
                   'ON_Texture::MODE', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_virtual=True)
    cls.add_method('ReverseTextureCoordinate', 
                   'bool', 
                   [param('int', 'dir')])
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('SwapTextureCoordinate', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('TileTextureCoordinate', 
                   'bool', 
                   [param('int', 'dir'), param('double', 'count'), param('double', 'offset')])
    cls.add_method('TypeFromInt', 
                   'ON_Texture::TYPE', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('WrapFromInt', 
                   'ON_Texture::WRAP', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_const=True, is_virtual=True)
    cls.add_static_attribute('m_ON_Texture_class_id', 'ON_ClassId const', is_const=True)
    cls.add_instance_attribute('m_bApply_uvw', 'bool', is_const=False)
    cls.add_instance_attribute('m_bOn', 'bool', is_const=False)
    cls.add_instance_attribute('m_blend_A', 'double [ 4 ]', is_const=False)
    cls.add_instance_attribute('m_blend_RGB', 'double [ 4 ]', is_const=False)
    cls.add_instance_attribute('m_blend_constant_A', 'double', is_const=False)
    cls.add_instance_attribute('m_blend_constant_RGB', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_blend_order', 'int', is_const=False)
    cls.add_instance_attribute('m_border_color', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_bump_scale', 'ON_Interval', is_const=False)
    cls.add_instance_attribute('m_filename', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_filename_bRelativePath', 'bool', is_const=False)
    cls.add_instance_attribute('m_magfilter', 'ON_Texture::FILTER', is_const=False)
    cls.add_instance_attribute('m_mapping_channel_id', 'int', is_const=False)
    cls.add_instance_attribute('m_minfilter', 'ON_Texture::FILTER', is_const=False)
    cls.add_instance_attribute('m_mode', 'ON_Texture::MODE', is_const=False)
    cls.add_instance_attribute('m_runtime_ptr', 'void const *', is_const=False)
    cls.add_instance_attribute('m_runtime_ptr_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_texture_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_transparency_texture_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_transparent_color', 'ON_Color', is_const=False)
    cls.add_instance_attribute('m_type', 'ON_Texture::TYPE', is_const=False)
    cls.add_instance_attribute('m_uvw', 'ON_Xform', is_const=False)
    cls.add_instance_attribute('m_wrapu', 'ON_Texture::WRAP', is_const=False)
    cls.add_instance_attribute('m_wrapv', 'ON_Texture::WRAP', is_const=False)
    cls.add_instance_attribute('m_wrapw', 'ON_Texture::WRAP', is_const=False)
    cls.add_method('DuplicateObject', 
                   'ON_Object *', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_ON_TextureCoordinates_methods(root_module, cls):
    cls.add_constructor([param('ON_TextureCoordinates const &', 'arg0')])
    cls.add_constructor([])
    cls.add_instance_attribute('m_T', 'ON_SimpleArray< ON_3fPoint >', is_const=False)
    cls.add_instance_attribute('m_dim', 'int', is_const=False)
    cls.add_instance_attribute('m_tag', 'ON_MappingTag', is_const=False)
    return

def register_ON_TextureMapping_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_TextureMapping const &', 'src')])
    cls.add_method('Cast', 
                   'ON_TextureMapping *', 
                   [param('ON_Object *', 'arg0')], 
                   is_static=True)
    cls.add_method('Cast', 
                   'ON_TextureMapping const *', 
                   [param('ON_Object const *', 'arg0')], 
                   is_static=True)
    cls.add_method('ClassId', 
                   'ON_ClassId const *', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Duplicate', 
                   'ON_TextureMapping *', 
                   [], 
                   is_const=True)
    cls.add_method('Evaluate', 
                   'int', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dVector const &', 'N'), param('ON_3dPoint *', 'T')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Evaluate', 
                   'int', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dVector const &', 'N'), param('ON_3dPoint *', 'T'), param('ON_Xform const &', 'P_xform'), param('ON_Xform const &', 'N_xform')], 
                   is_const=True, is_virtual=True)
    cls.add_method('EvaluateBoxMapping', 
                   'int', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dVector const &', 'N'), param('ON_3dPoint *', 'T')], 
                   is_const=True)
    cls.add_method('EvaluateCylinderMapping', 
                   'int', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dVector const &', 'N'), param('ON_3dPoint *', 'T')], 
                   is_const=True)
    cls.add_method('EvaluatePlaneMapping', 
                   'int', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dVector const &', 'N'), param('ON_3dPoint *', 'T')], 
                   is_const=True)
    cls.add_method('EvaluateSphereMapping', 
                   'int', 
                   [param('ON_3dPoint const &', 'P'), param('ON_3dVector const &', 'N'), param('ON_3dPoint *', 'T')], 
                   is_const=True)
    cls.add_method('GetMappingBox', 
                   'bool', 
                   [param('ON_Plane &', 'plane'), param('ON_Interval &', 'dx'), param('ON_Interval &', 'dy'), param('ON_Interval &', 'dz')], 
                   is_const=True)
    cls.add_method('GetMappingCylinder', 
                   'bool', 
                   [param('ON_Cylinder &', 'cylinder')], 
                   is_const=True)
    cls.add_method('GetMappingPlane', 
                   'bool', 
                   [param('ON_Plane &', 'plane'), param('ON_Interval &', 'dx'), param('ON_Interval &', 'dy'), param('ON_Interval &', 'dz')], 
                   is_const=True)
    cls.add_method('GetMappingSphere', 
                   'bool', 
                   [param('ON_Sphere &', 'sphere')], 
                   is_const=True)
    cls.add_method('GetTextureCoordinates', 
                   'bool', 
                   [param('ON_Mesh const &', 'mesh'), param('ON_SimpleArray< ON_3fPoint > &', 'T'), param('ON_Xform const *', 'mesh_xform', default_value='0'), param('bool', 'bLazy', default_value='false'), param('ON_SimpleArray< int > *', 'Tside', default_value='0')], 
                   is_const=True)
    cls.add_method('GetTextureCoordinates', 
                   'bool', 
                   [param('ON_Mesh const &', 'mesh'), param('ON_SimpleArray< ON_2fPoint > &', 'T'), param('ON_Xform const *', 'mesh_xform', default_value='0'), param('bool', 'bLazy', default_value='false'), param('ON_SimpleArray< int > *', 'Tside', default_value='0')], 
                   is_const=True)
    cls.add_method('HasMatchingTextureCoordinates', 
                   'bool', 
                   [param('ON_Mesh const &', 'mesh'), param('ON_Xform const *', 'object_xform', default_value='0')], 
                   is_const=True)
    cls.add_method('HasMatchingTextureCoordinates', 
                   'bool', 
                   [param('ON_MappingTag const &', 'tag'), param('ON_Xform const *', 'object_xform', default_value='0')], 
                   is_const=True)
    cls.add_method('IsPeriodic', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True, is_virtual=True)
    cls.add_method('MappingCRC', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    cls.add_method('ModelObjectId', 
                   'ON_UUID', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('ProjectionFromInt', 
                   'ON_TextureMapping::PROJECTION', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_virtual=True)
    cls.add_method('RequiresVertexNormals', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('ReverseTextureCoordinate', 
                   'bool', 
                   [param('int', 'dir')])
    cls.add_method('SetBoxMapping', 
                   'bool', 
                   [param('ON_Plane const &', 'plane'), param('ON_Interval', 'dx'), param('ON_Interval', 'dy'), param('ON_Interval', 'dz'), param('bool', 'bIsCapped')])
    cls.add_method('SetCylinderMapping', 
                   'bool', 
                   [param('ON_Cylinder const &', 'cylinder'), param('bool', 'bIsCapped')])
    cls.add_method('SetPlaneMapping', 
                   'bool', 
                   [param('ON_Plane const &', 'plane'), param('ON_Interval const &', 'dx'), param('ON_Interval const &', 'dy'), param('ON_Interval const &', 'dz')])
    cls.add_method('SetSphereMapping', 
                   'bool', 
                   [param('ON_Sphere const &', 'sphere')])
    cls.add_method('SetSurfaceParameterMapping', 
                   'bool', 
                   [])
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('SwapTextureCoordinate', 
                   'bool', 
                   [param('int', 'i'), param('int', 'j')])
    cls.add_method('TextureSpaceFromInt', 
                   'ON_TextureMapping::TEXTURE_SPACE', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('TileTextureCoordinate', 
                   'bool', 
                   [param('int', 'dir'), param('double', 'count'), param('double', 'offset')])
    cls.add_method('TypeFromInt', 
                   'ON_TextureMapping::TYPE', 
                   [param('int', 'i')], 
                   is_static=True)
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_const=True, is_virtual=True)
    cls.add_instance_attribute('m_Nxyz', 'ON_Xform', is_const=False)
    cls.add_static_attribute('m_ON_TextureMapping_class_id', 'ON_ClassId const', is_const=True)
    cls.add_instance_attribute('m_Pxyz', 'ON_Xform', is_const=False)
    cls.add_instance_attribute('m_bCapped', 'bool', is_const=False)
    cls.add_instance_attribute('m_mapping_id', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_mapping_index', 'int', is_const=False)
    cls.add_instance_attribute('m_mapping_name', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_mapping_primitive', 'ON_Object *', is_const=False)
    cls.add_instance_attribute('m_projection', 'ON_TextureMapping::PROJECTION', is_const=False)
    cls.add_instance_attribute('m_texture_space', 'ON_TextureMapping::TEXTURE_SPACE', is_const=False)
    cls.add_instance_attribute('m_type', 'ON_TextureMapping::TYPE', is_const=False)
    cls.add_instance_attribute('m_uvw', 'ON_Xform', is_const=False)
    cls.add_method('DuplicateObject', 
                   'ON_Object *', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_ON_Torus_methods(root_module, cls):
    cls.add_constructor([param('ON_Torus const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON_Plane const &', 'major__plane'), param('double', 'major__radius'), param('double', 'minor__radius')])
    cls.add_constructor([param('ON_Circle const &', 'major__circle'), param('double', 'minor__radius')])
    cls.add_method('Axis', 
                   'ON_3dVector', 
                   [], 
                   is_const=True)
    cls.add_method('Center', 
                   'ON_3dPoint', 
                   [], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_BOOL32', 
                   [param('ON_3dPoint', 'test_point'), param('double *', 'major_angle_radians'), param('double *', 'minor_angle_radians')], 
                   is_const=True)
    cls.add_method('ClosestPointTo', 
                   'ON_3dPoint', 
                   [param('ON_3dPoint', 'test_point')], 
                   is_const=True)
    cls.add_method('Create', 
                   'ON_BOOL32', 
                   [param('ON_Plane const &', 'major__plane'), param('double', 'major__radius'), param('double', 'minor__radius')])
    cls.add_method('Create', 
                   'ON_BOOL32', 
                   [param('ON_Circle const &', 'major__circle'), param('double', 'minor__radius')])
    cls.add_method('GetNurbForm', 
                   'int', 
                   [param('ON_NurbsSurface &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True)
    cls.add_method('MajorCircleDegrees', 
                   'ON_Circle', 
                   [param('double', 'minor_angle_degrees')], 
                   is_const=True)
    cls.add_method('MajorCircleRadians', 
                   'ON_Circle', 
                   [param('double', 'minor_angle_radians')], 
                   is_const=True)
    cls.add_method('MajorRadius', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('MinorCircleDegrees', 
                   'ON_Circle', 
                   [param('double', 'major_angle_degrees')], 
                   is_const=True)
    cls.add_method('MinorCircleRadians', 
                   'ON_Circle', 
                   [param('double', 'major_angle_radians')], 
                   is_const=True)
    cls.add_method('MinorRadius', 
                   'double', 
                   [], 
                   is_const=True)
    cls.add_method('NormalAt', 
                   'ON_3dVector', 
                   [param('double', 'major_angle_radians'), param('double', 'minor_angle_radians')], 
                   is_const=True)
    cls.add_method('PointAt', 
                   'ON_3dPoint', 
                   [param('double', 'major_angle_radians'), param('double', 'minor_angle_radians')], 
                   is_const=True)
    cls.add_method('RevSurfaceForm', 
                   'ON_RevSurface *', 
                   [param('ON_RevSurface *', 'srf', default_value='0')], 
                   is_const=True)
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'angle_radians'), param('ON_3dVector const &', 'axis_of_rotation')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'sin_angle'), param('double', 'cos_angle'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Rotate', 
                   'ON_BOOL32', 
                   [param('double', 'angle_radians'), param('ON_3dVector const &', 'axis_of_rotation'), param('ON_3dPoint const &', 'center_of_rotation')])
    cls.add_method('Transform', 
                   'ON_BOOL32', 
                   [param('ON_Xform const &', 'arg0')])
    cls.add_method('Translate', 
                   'ON_BOOL32', 
                   [param('ON_3dVector const &', 'arg0')])
    cls.add_instance_attribute('major_radius', 'double', is_const=False)
    cls.add_instance_attribute('minor_radius', 'double', is_const=False)
    cls.add_instance_attribute('plane', 'ON_Plane', is_const=False)
    return

def register_ON_U_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_U const &', 'arg0')])
    cls.add_instance_attribute('b', 'char [ 8 ]', is_const=False)
    cls.add_instance_attribute('d', 'double', is_const=False)
    cls.add_instance_attribute('h', 'ON__INT64', is_const=False)
    cls.add_instance_attribute('i', 'ON__INT32', is_const=False)
    cls.add_instance_attribute('j', 'int [ 2 ]', is_const=False)
    cls.add_instance_attribute('p', 'void *', is_const=False)
    return

def register_ON_UUID_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([])
    cls.add_constructor([param('ON_UUID const &', 'arg0')])
    cls.add_instance_attribute('Data1', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('Data2', 'ON__UINT16', is_const=False)
    cls.add_instance_attribute('Data3', 'ON__UINT16', is_const=False)
    cls.add_instance_attribute('Data4', 'unsigned char [ 8 ]', is_const=False)
    return

def register_ON_UncompressStream_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_method('SetCallback', 
                   'bool', 
                   [param('ON_StreamCallbackFunction', 'callback_function'), param('void *', 'callback_context')])
    cls.add_method('CallbackFunction', 
                   'ON_StreamCallbackFunction', 
                   [], 
                   is_const=True)
    cls.add_method('CallbackContext', 
                   'void *', 
                   [], 
                   is_const=True)
    cls.add_method('Begin', 
                   'bool', 
                   [])
    cls.add_method('In', 
                   'bool', 
                   [param('ON__UINT64', 'in_buffer_size'), param('void const *', 'in_buffer')])
    cls.add_method('Out', 
                   'bool', 
                   [param('void *', 'callback_context'), param('ON__UINT32', 'out_buffer_size'), param('void const *', 'out_buffer')], 
                   is_virtual=True)
    cls.add_method('End', 
                   'bool', 
                   [])
    cls.add_method('InSize', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('OutSize', 
                   'ON__UINT64', 
                   [], 
                   is_const=True)
    cls.add_method('InCRC', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    cls.add_method('OutCRC', 
                   'ON__UINT32', 
                   [], 
                   is_const=True)
    return

def register_ON_UnicodeErrorParameters_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_UnicodeErrorParameters const &', 'arg0')])
    cls.add_instance_attribute('m_error_code_point', 'ON__UINT32', is_const=False)
    cls.add_instance_attribute('m_error_mask', 'unsigned int', is_const=False)
    cls.add_instance_attribute('m_error_status', 'unsigned int', is_const=False)
    return

def register_ON_UnitSystem_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('!=')
    cls.add_constructor([param('ON_UnitSystem const &', 'arg0')])
    cls.add_constructor([])
    cls.add_constructor([param('ON::unit_system', 'arg0')])
    cls.add_method('Default', 
                   'void', 
                   [])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'arg0')], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'bool', 
                   [], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_custom_unit_name', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_custom_unit_scale', 'double', is_const=False)
    cls.add_instance_attribute('m_unit_system', 'ON::unit_system', is_const=False)
    return

def register_ON_UserData_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_UserData const &', 'arg0')])
    cls.add_method('Archive', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Cast', 
                   'ON_UserData *', 
                   [param('ON_Object *', 'arg0')], 
                   is_static=True)
    cls.add_method('Cast', 
                   'ON_UserData const *', 
                   [param('ON_Object const *', 'arg0')], 
                   is_static=True)
    cls.add_method('ClassId', 
                   'ON_ClassId const *', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Duplicate', 
                   'ON_UserData *', 
                   [], 
                   is_const=True)
    cls.add_method('GetDescription', 
                   'ON_BOOL32', 
                   [param('ON_wString &', 'description')], 
                   is_virtual=True)
    cls.add_method('IsUnknownUserData', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True)
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Next', 
                   'ON_UserData *', 
                   [], 
                   is_const=True)
    cls.add_method('Owner', 
                   'ON_Object *', 
                   [], 
                   is_const=True)
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Transform', 
                   'ON_BOOL32', 
                   [param('ON_Xform const &', 'arg0')], 
                   is_virtual=True)
    cls.add_method('UserDataClassUuid', 
                   'ON_UUID', 
                   [], 
                   is_const=True)
    cls.add_static_attribute('m_ON_UserData_class_id', 'ON_ClassId const', is_const=True)
    cls.add_instance_attribute('m_application_uuid', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_userdata_copycount', 'unsigned int', is_const=False)
    cls.add_instance_attribute('m_userdata_uuid', 'ON_UUID', is_const=False)
    cls.add_instance_attribute('m_userdata_xform', 'ON_Xform', is_const=False)
    cls.add_method('DuplicateObject', 
                   'ON_Object *', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_ON_UserDataHolder_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('ON_UserDataHolder const &', 'arg0')])
    cls.add_method('IsValid', 
                   'ON_BOOL32', 
                   [param('ON_TextLog *', 'text_log', default_value='0')], 
                   is_const=True, is_virtual=True)
    cls.add_method('MoveUserDataFrom', 
                   'bool', 
                   [param('ON_Object const &', 'source_object')])
    cls.add_method('MoveUserDataTo', 
                   'bool', 
                   [param('ON_Object const &', 'source_object'), param('bool', 'bAppend')])
    return

def register_ON_UserString_methods(root_module, cls):
    cls.add_constructor([param('ON_UserString const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True)
    cls.add_method('Read', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')])
    cls.add_method('Write', 
                   'bool', 
                   [param('ON_BinaryArchive &', 'arg0')], 
                   is_const=True)
    cls.add_instance_attribute('m_key', 'ON_wString', is_const=False)
    cls.add_instance_attribute('m_string_value', 'ON_wString', is_const=False)
    return

def register_ON_UserStringList_methods(root_module, cls):
    cls.add_constructor([param('ON_UserStringList const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('Archive', 
                   'ON_BOOL32', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Cast', 
                   'ON_UserStringList *', 
                   [param('ON_Object *', 'arg0')], 
                   is_static=True)
    cls.add_method('Cast', 
                   'ON_UserStringList const *', 
                   [param('ON_Object const *', 'arg0')], 
                   is_static=True)
    cls.add_method('ClassId', 
                   'ON_ClassId const *', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('DataCRC', 
                   'ON__UINT32', 
                   [param('ON__UINT32', 'current_remainder')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Dump', 
                   'void', 
                   [param('ON_TextLog &', 'text_log')], 
                   is_const=True, is_virtual=True)
    cls.add_method('Duplicate', 
                   'ON_UserStringList *', 
                   [], 
                   is_const=True)
    cls.add_method('GetDescription', 
                   'ON_BOOL32', 
                   [param('ON_wString &', 'description')], 
                   is_virtual=True)
    cls.add_method('GetUserString', 
                   'bool', 
                   [param('wchar_t const *', 'key'), param('ON_wString &', 'string_value')], 
                   is_const=True)
    cls.add_method('Read', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_virtual=True)
    cls.add_method('SetUserString', 
                   'bool', 
                   [param('wchar_t const *', 'key'), param('wchar_t const *', 'string_value')])
    cls.add_method('SetUserStrings', 
                   'int', 
                   [param('int', 'count'), param('ON_UserString const *', 'us'), param('bool', 'bReplace')])
    cls.add_method('SizeOf', 
                   'unsigned int', 
                   [], 
                   is_const=True, is_virtual=True)
    cls.add_method('Write', 
                   'ON_BOOL32', 
                   [param('ON_BinaryArchive &', 'binary_archive')], 
                   is_const=True, is_virtual=True)
    cls.add_static_attribute('m_ON_UserStringList_class_id', 'ON_ClassId const', is_const=True)
    cls.add_instance_attribute('m_e', 'ON_ClassArray< ON_UserString >', is_const=False)
    cls.add_method('DuplicateObject', 
                   'ON_Object *', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_ON_UuidIndex_methods(root_module, cls):
    cls.add_constructor([param('ON_UuidIndex const &', 'arg0')])
    cls.add_constructor([])
    cls.add_method('CompareId', 
                   'int', 
                   [param('ON_UuidIndex const *', 'a'), param('ON_UuidIndex const *', 'b')], 
                   is_static=True)
    cls.add_method('CompareIdAndIndex', 
                   'int', 
                   [param('ON_UuidIndex const *', 'a'), param('ON_UuidIndex const *', 'b')], 
                   is_static=True)
    cls.add_method('CompareIndex', 
                   'int', 
                   [param('ON_UuidIndex const *', 'a'), param('ON_UuidIndex const *', 'b')], 
                   is_static=True)
    cls.add_method('CompareIndexAndId', 
                   'int', 
                   [param('ON_UuidIndex const *', 'a'), param('ON_UuidIndex const *', 'b')], 
                   is_static=True)
    cls.add_instance_attribute('m_i', 'int', is_const=False)
    cls.add_instance_attribute('m_id', 'ON_UUID', is_const=False)
    return

def register_ON_UuidIndexList_methods(root_module, cls):
    cls.add_constructor([])
    cls.add_constructor([param('int', 'capacity')])
    cls.add_constructor([param('ON_UuidIndexList const &', 'src')])
    cls.add_method('AddUuidIndex', 
                   'bool', 
                   [param('ON_UUID', 'uuid'), param('int', 'index'), param('bool', 'bCheckForDupicates', default_value='true')])
    cls.add_method('Count', 
                   'int', 
                   [], 
                   is_const=True)
    cls.add_method('Empty', 
                   'void', 
                   [])
    cls.add_method('FindUuid', 
                   'bool', 
                   [param('ON_UUID', 'uuid'), param('int *', 'index', default_value='0')], 
                   is_const=True)
