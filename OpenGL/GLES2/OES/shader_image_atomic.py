'''OpenGL extension OES.shader_image_atomic

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.shader_image_atomic to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/shader_image_atomic.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.shader_image_atomic import *
from OpenGL.raw.GLES2.OES.shader_image_atomic import _EXTENSION_NAME

def glInitShaderImageAtomicOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION