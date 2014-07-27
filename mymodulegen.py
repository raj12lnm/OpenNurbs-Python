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
    root_module = Module('mymodule', cpp_namespace='::')
    root_module.add_include('"examples_linking_pragmas.h"')
    root_module.add_include('"opennurbs_3dm_attributes.h"')
    root_module.add_include('"opennurbs_3dm.h"')
    root_module.add_include('"opennurbs_3dm_properties.h"')
    root_module.add_include('"opennurbs_3dm_settings.h"')
    root_module.add_include('"opennurbs_annotation2.h"')
    root_module.add_include('"opennurbs_annotation.h"')
    root_module.add_include('"opennurbs_arccurve.h"')
    root_module.add_include('"opennurbs_arc.h"')
    root_module.add_include('"opennurbs_archive.h"')
    root_module.add_include('"opennurbs_array_defs.h"')
    root_module.add_include('"opennurbs_array.h"')
    root_module.add_include('"opennurbs_base32.h"')
    root_module.add_include('"opennurbs_base64.h"')
    root_module.add_include('"opennurbs_beam.h"')
    root_module.add_include('"opennurbs_bezier.h"')
    root_module.add_include('"opennurbs_bitmap.h"')
    root_module.add_include('"opennurbs_bounding_box.h"')
    root_module.add_include('"opennurbs_box.h"')
    root_module.add_include('"opennurbs_brep.h"')
    root_module.add_include('"opennurbs_circle.h"')
    root_module.add_include('"opennurbs_color.h"')
    root_module.add_include('"opennurbs_compress.h"')
    root_module.add_include('"opennurbs_cone.h"')
    root_module.add_include('"opennurbs_crc.h"')
    root_module.add_include('"opennurbs_curve.h"')
    root_module.add_include('"opennurbs_curveonsurface.h"')
    root_module.add_include('"opennurbs_curveproxy.h"')
    root_module.add_include('"opennurbs_cylinder.h"')
    root_module.add_include('"opennurbs_defines.h"')
    root_module.add_include('"opennurbs_detail.h"')
    root_module.add_include('"opennurbs_dimstyle.h"')
    root_module.add_include('"opennurbs_dll_resource.h"')
    root_module.add_include('"opennurbs_ellipse.h"')
    root_module.add_include('"opennurbs_error.h"')
    root_module.add_include('"opennurbs_evaluate_nurbs.h"')
    root_module.add_include('"opennurbs_extensions.h"')
    root_module.add_include('"opennurbs_font.h"')
    root_module.add_include('"opennurbs_fpoint.h"')
    root_module.add_include('"opennurbs_fsp_defs.h"')
    root_module.add_include('"opennurbs_fsp.h"')
    root_module.add_include('"opennurbs_geometry.h"')
    root_module.add_include('"opennurbs_gl.h"')
    root_module.add_include('"opennurbs_group.h"')
    root_module.add_include('"opennurbs.h"')
    root_module.add_include('"opennurbs_hatch.h"')
    root_module.add_include('"opennurbs_hsort_template.h"')
    root_module.add_include('"opennurbs_instance.h"')
    root_module.add_include('"opennurbs_intersect.h"')
    root_module.add_include('"opennurbs_knot.h"')
    root_module.add_include('"opennurbs_layer.h"')
    root_module.add_include('"opennurbs_light.h"')
    root_module.add_include('"opennurbs_linecurve.h"')
    root_module.add_include('"opennurbs_line.h"')
    root_module.add_include('"opennurbs_linestyle.h"')
    root_module.add_include('"opennurbs_linetype.h"')
    root_module.add_include('"opennurbs_lookup.h"')
    root_module.add_include('"opennurbs_mapchan.h"')
    root_module.add_include('"opennurbs_massprop.h"')
    root_module.add_include('"opennurbs_material.h"')
    root_module.add_include('"opennurbs_math.h"')
    root_module.add_include('"opennurbs_matrix.h"')
    root_module.add_include('"opennurbs_memory.h"')
    root_module.add_include('"opennurbs_mesh.h"')
    root_module.add_include('"opennurbs_nurbscurve.h"')
    root_module.add_include('"opennurbs_nurbssurface.h"')
    root_module.add_include('"opennurbs_object.h"')
    root_module.add_include('"opennurbs_object_history.h"')
    root_module.add_include('"opennurbs_objref.h"')
    root_module.add_include('"opennurbs_optimize.h"')
    root_module.add_include('"opennurbs_offsetsurface.h"')
    root_module.add_include('"opennurbs_plane.h"')
    root_module.add_include('"opennurbs_planesurface.h"')
    root_module.add_include('"opennurbs_pluginlist.h"')
    root_module.add_include('"opennurbs_pointcloud.h"')
    root_module.add_include('"opennurbs_pointgeometry.h"')
    root_module.add_include('"opennurbs_pointgrid.h"')
    root_module.add_include('"opennurbs_point.h"')
    root_module.add_include('"opennurbs_polycurve.h"')
    root_module.add_include('"opennurbs_polyedgecurve.h"')
    root_module.add_include('"opennurbs_polylinecurve.h"')
    root_module.add_include('"opennurbs_polyline.h"')
    root_module.add_include('"opennurbs_qsort_template.h"')
    root_module.add_include('"opennurbs_rand.h"')
    root_module.add_include('"opennurbs_rendering.h"')
    root_module.add_include('"opennurbs_revsurface.h"')
    root_module.add_include('"opennurbs_rtree.h"')
    root_module.add_include('"opennurbs_sphere.h"')
    root_module.add_include('"opennurbs_string.h"')
    root_module.add_include('"opennurbs_sumsurface.h"')
    root_module.add_include('"opennurbs_surface.h"')
    root_module.add_include('"opennurbs_surfaceproxy.h"')
    root_module.add_include('"opennurbs_system.h"')
    root_module.add_include('"opennurbs_textlog.h"')
    root_module.add_include('"opennurbs_texture.h"')
    root_module.add_include('"opennurbs_texture_mapping.h"')
    root_module.add_include('"opennurbs_torus.h"')
    root_module.add_include('"opennurbs_unicode.h"')
    root_module.add_include('"opennurbs_userdata.h"')
    root_module.add_include('"opennurbs_uuid.h"')
    root_module.add_include('"opennurbs_version.h"')
    root_module.add_include('"opennurbs_viewport.h"')
    root_module.add_include('"opennurbs_workspace.h"')
    root_module.add_include('"opennurbs_xform.h"')
    root_module.add_include('"opennurbs_x.h"')
    root_module.add_include('"opennurbs_zlib.h"')
    return root_module

def register_types(module):
    root_module = module.get_root()
    
    
    ## Register a nested module for the namespace std
    
    nested_module = module.add_cpp_namespace('std')
    register_types_std(nested_module)
    

def register_types_std(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    return

def register_functions(root_module):
    module = root_module
    register_functions_std(module.get_submodule('std'), root_module)
    return

def register_functions_std(module, root_module):
    return

def main():
    out = FileCodeSink(sys.stdout)
    root_module = module_init()
    register_types(root_module)
    register_methods(root_module)
    register_functions(root_module)
    root_module.generate(out)

if __name__ == '__main__':
    main()

