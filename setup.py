#!/usr/bin/env python
import os
from distutils.core import setup, Extension
import mymodulegen as generate

try:
    os.mkdir("build")
except OSError:
    pass
module_fname = os.path.join("build", "my-module-binding.cpp")
#with open(module_fname, "wt") as file_:
#    print("Generating file {}".format(module_fname))
#    generate(file_)

mymodule = Extension('mymodule',
                     sources = [module_fname,
                                'opennurbs_3dm_attributes.cpp','opennurbs_3dm_properties.cpp','opennurbs_3dm_settings.cpp','opennurbs_annotation2.cpp','opennurbs_annotation.cpp','opennurbs_arc.cpp','opennurbs_arccurve.cpp','opennurbs_archive.cpp','opennurbs_array.cpp','opennurbs_base32.cpp','opennurbs_base64.cpp','opennurbs_basic.cpp','opennurbs_beam.cpp','opennurbs_bezier.cpp','opennurbs_beziervolume.cpp','opennurbs_bitmap.cpp','opennurbs_bounding_box.cpp','opennurbs_box.cpp','opennurbs_brep_changesrf.cpp','opennurbs_brep.cpp','opennurbs_brep_extrude.cpp','opennurbs_brep_io.cpp','opennurbs_brep_isvalid.cpp','opennurbs_brep_kinky.cpp','opennurbs_brep_region.cpp','opennurbs_brep_tools.cpp','opennurbs_brep_v2valid.cpp','opennurbs_circle.cpp','opennurbs_color.cpp','opennurbs_compress.cpp','opennurbs_cone.cpp','opennurbs_crc.cpp','opennurbs_curve.cpp','opennurbs_curveonsurface.cpp','opennurbs_curveproxy.cpp','opennurbs_cylinder.cpp','opennurbs_defines.cpp','opennurbs_detail.cpp','opennurbs_dimstyle.cpp','opennurbs_dll.cpp','opennurbs_ellipse.cpp','opennurbs_embedded_file.cpp','opennurbs_error.cpp','opennurbs_error_message.cpp','opennurbs_evaluate_nurbs.cpp','opennurbs_extensions.cpp','opennurbs_font.cpp','opennurbs_fsp.cpp','opennurbs_geometry.cpp','opennurbs_gl.cpp','opennurbs_group.cpp','opennurbs_hatch.cpp','opennurbs_instance.cpp','opennurbs_intersect.cpp','opennurbs_knot.cpp','opennurbs_layer.cpp','opennurbs_light.cpp','opennurbs_line.cpp','opennurbs_linecurve.cpp','opennurbs_linetype.cpp','opennurbs_lookup.cpp','opennurbs_massprop.cpp','opennurbs_material.cpp','opennurbs_math.cpp','opennurbs_matrix.cpp','opennurbs_mesh.cpp','opennurbs_mesh_ngon.cpp','opennurbs_mesh_tools.cpp','opennurbs_morph.cpp','opennurbs_nurbscurve.cpp','opennurbs_nurbssurface.cpp','opennurbs_nurbsvolume.cpp','opennurbs_object.cpp','opennurbs_object_history.cpp','opennurbs_objref.cpp','opennurbs_offsetsurface.cpp','opennurbs_optimize.cpp','opennurbs_plane.cpp','opennurbs_planesurface.cpp','opennurbs_pluginlist.cpp','opennurbs_pointcloud.cpp','opennurbs_point.cpp','opennurbs_pointgeometry.cpp','opennurbs_pointgrid.cpp','opennurbs_polycurve.cpp','opennurbs_polyedgecurve.cpp','opennurbs_polyline.cpp','opennurbs_polylinecurve.cpp','opennurbs_precompiledheader.cpp','opennurbs_rand.cpp','opennurbs_revsurface.cpp','opennurbs_rtree.cpp','opennurbs_sort.cpp','opennurbs_sphere.cpp','opennurbs_string.cpp','opennurbs_sum.cpp','opennurbs_sumsurface.cpp','opennurbs_surface.cpp','opennurbs_surfaceproxy.cpp','opennurbs_textlog.cpp','opennurbs_torus.cpp','opennurbs_unicode.cpp','opennurbs_userdata.cpp','opennurbs_uuid.cpp','opennurbs_viewport.cpp','opennurbs_workspace.cpp','opennurbs_wstring.cpp','opennurbs_x.cpp','opennurbs_xform.cpp','opennurbs_zlib.cpp','opennurbs_zlib_memory.cpp'],
                     include_dirs=['.'])

setup(name='PyBindGen-example',
      version="0.0",
      description='PyBindGen example',
      author='xxx',
      author_email='yyy@zz',
      ext_modules=[mymodule],
     )

