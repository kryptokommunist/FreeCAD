import Part, math
import FreeCAD, FreeCADGui
import WorkingPlane
App=FreeCAD
Gui=FreeCADGui
from FreeCAD import Base, Vector
from draftviewproviders.view_base import _ViewProviderDraft
from draftutils.gui_utils import select
from draftutils.translate import translate
from PySide.QtCore import QT_TRANSLATE_NOOP
import DraftVecUtils

from draftutils.utils import getParam
from draftutils.utils import typecheck

from draftutils.utils import typecheck
from draftutils.utils import type_check

from draftutils.utils import getParamType
from draftutils.utils import get_param_type

from draftutils.utils import getParam
from draftutils.utils import get_param

from draftutils.utils import setParam
from draftutils.utils import set_param

from draftutils.utils import precision
from draftutils.utils import tolerance
from draftutils.utils import epsilon

from draftutils.utils import getRealName
from draftutils.utils import get_real_name

from draftutils.utils import getType
from draftutils.utils import get_type

from draftutils.utils import getObjectsOfType
from draftutils.utils import get_objects_of_type

from draftutils.utils import isClone
from draftutils.utils import is_clone

from draftutils.utils import getGroupNames
from draftutils.utils import get_group_names

from draftutils.utils import ungroup

from draftutils.utils import getGroupContents
from draftutils.utils import get_group_contents

from draftutils.utils import printShape
from draftutils.utils import print_shape

from draftutils.utils import compareObjects
from draftutils.utils import compare_objects

from draftutils.utils import shapify

from draftutils.utils import loadSvgPatterns
from draftutils.utils import load_svg_patterns

from draftutils.utils import svgpatterns
from draftutils.utils import svg_patterns

from draftutils.utils import getMovableChildren
from draftutils.utils import get_movable_children

from draftutils.gui_utils import get3DView
from draftutils.gui_utils import get_3d_view

from draftutils.gui_utils import autogroup

from draftutils.gui_utils import dimSymbol
from draftutils.gui_utils import dim_symbol

from draftutils.gui_utils import dimDash
from draftutils.gui_utils import dim_dash

from draftutils.gui_utils import removeHidden
from draftutils.gui_utils import remove_hidden

from draftutils.gui_utils import formatObject
from draftutils.gui_utils import format_object

from draftutils.gui_utils import getSelection
from draftutils.gui_utils import get_selection

from draftutils.gui_utils import getSelectionEx
from draftutils.gui_utils import get_selection_ex

from draftutils.gui_utils import select

from draftutils.gui_utils import loadTexture
from draftutils.gui_utils import load_texture

#---------------------------------------------------------------------------
# Draft objects
#---------------------------------------------------------------------------

# base object
from draftobjects.base import DraftObject
from draftobjects.base import _DraftObject

# base viewprovider
from draftviewproviders.view_base import ViewProviderDraft
from draftviewproviders.view_base import _ViewProviderDraft
from draftviewproviders.view_base import ViewProviderDraftAlt
from draftviewproviders.view_base import _ViewProviderDraftAlt
from draftviewproviders.view_base import ViewProviderDraftPart
from draftviewproviders.view_base import _ViewProviderDraftPart

# circle
from draftmake.make_circle import make_circle, makeCircle
from draftobjects.circle import Circle, _Circle

# ellipse
from draftmake.make_ellipse import make_ellipse, makeEllipse
from draftobjects.ellipse import Ellipse, _Ellipse

# rectangle
from draftmake.make_rectangle import make_rectangle, makeRectangle
from draftobjects.rectangle import Rectangle, _Rectangle
if FreeCAD.GuiUp:
    from draftviewproviders.view_rectangle import ViewProviderRectangle
    from draftviewproviders.view_rectangle import _ViewProviderRectangle

# polygon
from draftmake.make_polygon import make_polygon, makePolygon
from draftobjects.polygon import Polygon, _Polygon

# wire and line
from draftmake.make_line import make_line, makeLine
from draftmake.make_wire import make_wire, makeWire
from draftobjects.wire import Wire, _Wire
if FreeCAD.GuiUp:
    from draftviewproviders.view_wire import ViewProviderWire
    from draftviewproviders.view_wire import _ViewProviderWire

# bspline
from draftmake.make_bspline import make_bspline, makeBSpline
from draftobjects.bspline import BSpline, _BSpline
if FreeCAD.GuiUp:
    from draftviewproviders.view_bspline import ViewProviderBSpline
    from draftviewproviders.view_bspline import _ViewProviderBSpline

# bezcurve
from draftmake.make_bezcurve import make_bezcurve, makeBezCurve
from draftobjects.bezcurve import BezCurve, _BezCurve
if FreeCAD.GuiUp:
    from draftviewproviders.view_bezcurve import ViewProviderBezCurve
    from draftviewproviders.view_bezcurve import _ViewProviderBezCurve

# clone
from draftmake.make_clone import make_clone, clone
from draftobjects.clone import Clone, _Clone
if FreeCAD.GuiUp:
    from draftviewproviders.view_clone import ViewProviderClone
    from draftviewproviders.view_clone import _ViewProviderClone

# point
from draftmake.make_point import make_point, makePoint
from draftobjects.point import Point, _Point
if FreeCAD.GuiUp:
    from draftviewproviders.view_point import ViewProviderPoint
    from draftviewproviders.view_point import _ViewProviderPoint

# facebinder
from draftmake.make_facebinder import make_facebinder, makeFacebinder
from draftobjects.facebinder import Facebinder, _Facebinder
if FreeCAD.GuiUp:
    from draftviewproviders.view_facebinder import ViewProviderFacebinder
    from draftviewproviders.view_facebinder import _ViewProviderFacebinder

# shapestring
from draftmake.make_block import make_block, makeBlock
from draftobjects.block import Block, _Block

# shapestring
from draftmake.make_shapestring import make_shapestring, makeShapeString
from draftobjects.shapestring import ShapeString, _ShapeString

# shape 2d view
from draftmake.make_shape2dview import make_shape2dview, makeShape2DView
from draftobjects.shape2dview import Shape2DView, _Shape2DView

# sketch
from draftmake.make_sketch import make_sketch, makeSketch

# working plane proxy
from draftmake.make_wpproxy import make_workingplaneproxy
from draftmake.make_wpproxy import makeWorkingPlaneProxy
from draftobjects.wpproxy import WorkingPlaneProxy
if FreeCAD.GuiUp:
    from draftviewproviders.view_wpproxy import ViewProviderWorkingPlaneProxy

if FreeCAD.GuiUp:
    import FreeCADGui
    import Draft_rc
    gui = True
    # To prevent complaints from code checkers (flake8)
    True if Draft_rc.__name__ else False
else:
    gui = False

#---------------------------------------------------------------------------
# Draft annotation objects
#---------------------------------------------------------------------------

from draftobjects.dimension import make_dimension, make_angular_dimension
from draftobjects.dimension import LinearDimension, AngularDimension

makeDimension = make_dimension
makeAngularDimension = make_angular_dimension
_Dimension = LinearDimension
_AngularDimension = AngularDimension

if gui:
    from draftviewproviders.view_dimension import ViewProviderLinearDimension
    from draftviewproviders.view_dimension import ViewProviderAngularDimension
    _ViewProviderDimension = ViewProviderLinearDimension
    _ViewProviderAngularDimension = ViewProviderAngularDimension


from draftobjects.label import make_label
from draftobjects.label import Label

makeLabel = make_label
DraftLabel = Label

if gui:
    from draftviewproviders.view_label import ViewProviderLabel
    ViewProviderDraftLabel = ViewProviderLabel


from draftobjects.text import make_text
from draftobjects.text import Text
makeText = make_text
DraftText = Text

if gui:
    from draftviewproviders.view_text import ViewProviderText
    ViewProviderDraftText = ViewProviderText



__title__ = "FreeCAD Part Array"
__author__ = ("Yorik van Havre, Werner Mayer, Martin Burbaum, Ken Cline, "
              "Dmitry Chigrin, Daniel Falck")
__url__ = "https://www.freecadweb.org"
gui = True

def array(objectslist,arg1,arg2,arg3,arg4=None,arg5=None,arg6=None):
    """array(objectslist,xvector,yvector,xnum,ynum) for rectangular array,
    array(objectslist,xvector,yvector,zvector,xnum,ynum,znum) for rectangular array,
    or array(objectslist,center,totalangle,totalnum) for polar array: Creates an array
    of the objects contained in list (that can be an object or a list of objects)
    with, in case of rectangular array, xnum of iterations in the x direction
    at xvector distance between iterations, and same for y and z directions with yvector
    and ynum and zvector and znum. In case of polar array, center is a vector, totalangle
    is the angle to cover (in degrees) and totalnum is the number of objects, including
    the original.

    This function creates an array of independent objects. Use makeArray() to create a
    parametric array object."""

    def rectArray(objectslist,xvector,yvector,xnum,ynum):
        typecheck([(xvector,Vector), (yvector,Vector), (xnum,int), (ynum,int)], "rectArray")
        if not isinstance(objectslist,list): objectslist = [objectslist]
        for xcount in range(xnum):
            currentxvector=Vector(xvector).multiply(xcount)
            if not xcount==0:
                move(objectslist,currentxvector,True)
            for ycount in range(ynum):
                currentxvector=FreeCAD.Base.Vector(currentxvector)
                currentyvector=currentxvector.add(Vector(yvector).multiply(ycount))
                if not ycount==0:
                    move(objectslist,currentyvector,True)
    def rectArray2(objectslist,xvector,yvector,zvector,xnum,ynum,znum):
        typecheck([(xvector,Vector), (yvector,Vector), (zvector,Vector),(xnum,int), (ynum,int),(znum,int)], "rectArray2")
        if not isinstance(objectslist,list): objectslist = [objectslist]
        for xcount in range(xnum):
            currentxvector=Vector(xvector).multiply(xcount)
            if not xcount==0:
                move(objectslist,currentxvector,True)
            for ycount in range(ynum):
                currentxvector=FreeCAD.Base.Vector(currentxvector)
                currentyvector=currentxvector.add(Vector(yvector).multiply(ycount))
                if not ycount==0:
                    move(objectslist,currentyvector,True)
                for zcount in range(znum):
                    currentzvector=currentyvector.add(Vector(zvector).multiply(zcount))
                    if not zcount==0:
                        move(objectslist,currentzvector,True)
    def polarArray(objectslist,center,angle,num):
        typecheck([(center,Vector), (num,int)], "polarArray")
        if not isinstance(objectslist,list): objectslist = [objectslist]
        fraction = float(angle)/num
        for i in range(num):
            currangle = fraction + (i*fraction)
            rotate(objectslist,currangle,center,copy=True)
    if arg6:
        rectArray2(objectslist,arg1,arg2,arg3,arg4,arg5,arg6)
    elif arg4:
        rectArray(objectslist,arg1,arg2,arg3,arg4)
    else:
        polarArray(objectslist,arg1,arg2,arg3)

def makeArray(baseobject,arg1,arg2,arg3,arg4=None,arg5=None,arg6=None,name="Array",use_link=False):
    """makeArray(object,xvector,yvector,xnum,ynum,[name]) for rectangular array, or
    makeArray(object,xvector,yvector,zvector,xnum,ynum,znum,[name]) for rectangular array, or
    makeArray(object,center,totalangle,totalnum,[name]) for polar array, or
    makeArray(object,rdistance,tdistance,axis,center,ncircles,symmetry,[name]) for circular array:
    Creates an array of the given object
    with, in case of rectangular array, xnum of iterations in the x direction
    at xvector distance between iterations, same for y direction with yvector and ynum,
    same for z direction with zvector and znum. In case of polar array, center is a vector,
    totalangle is the angle to cover (in degrees) and totalnum is the number of objects,
    including the original. In case of a circular array, rdistance is the distance of the
    circles, tdistance is the distance within circles, axis the rotation-axes, center the
    center of rotation, ncircles the number of circles and symmetry the number
    of symmetry-axis of the distribution. The result is a parametric Draft Array.
    """

    if not FreeCAD.ActiveDocument:
        FreeCAD.Console.PrintError("No active document. Aborting\n")
        return
    if use_link:
        obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython",name,_Array(None),None,True)
    else:
        obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython",name)
        _Array(obj)
    obj.Base = baseobject
    if arg6:
        if isinstance(arg1, (int, float, FreeCAD.Units.Quantity)):
            obj.ArrayType = "circular"
            obj.RadialDistance = arg1
            obj.TangentialDistance = arg2
            obj.Axis = arg3
            obj.Center = arg4
            obj.NumberCircles = arg5
            obj.Symmetry = arg6
        else:
            obj.ArrayType = "ortho"
            obj.IntervalX = arg1
            obj.IntervalY = arg2
            obj.IntervalZ = arg3
            obj.NumberX = arg4
            obj.NumberY = arg5
            obj.NumberZ = arg6
    elif arg4:
        obj.ArrayType = "ortho"
        obj.IntervalX = arg1
        obj.IntervalY = arg2
        obj.NumberX = arg3
        obj.NumberY = arg4
    else:
        obj.ArrayType = "polar"
        obj.Center = arg1
        obj.Angle = arg2
        obj.NumberPolar = arg3
    if gui:
        if use_link:
            _ViewProviderDraftLink(obj.ViewObject)
        else:
            _ViewProviderDraftArray(obj.ViewObject)
            formatObject(obj,obj.Base)
            if len(obj.Base.ViewObject.DiffuseColor) > 1:
                obj.ViewObject.Proxy.resetColors(obj.ViewObject)
        baseobject.ViewObject.hide()
        select(obj)
    return obj

class _DraftLink(_DraftObject):

    def __init__(self,obj,tp):
        self.use_link = False if obj else True
        _DraftObject.__init__(self,obj,tp)
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self,state):
        if isinstance(state,dict):
            self.__dict__ = state
        else:
            self.use_link = False
            _DraftObject.__setstate__(self,state)

    def attach(self,obj):
        if self.use_link:
            obj.addExtension('App::LinkExtensionPython', None)
            self.linkSetup(obj)

    def canLinkProperties(self,_obj):
        return False

    def linkSetup(self,obj):
        obj.configLinkProperty('Placement',LinkedObject='Base')
        if hasattr(obj,'ShowElement'):
            # rename 'ShowElement' property to 'ExpandArray' to avoid conflict
            # with native App::Link
            obj.configLinkProperty('ShowElement')
            showElement = obj.ShowElement
            obj.addProperty("App::PropertyBool","ExpandArray","Draft",
                    QT_TRANSLATE_NOOP("App::Property","Show array element as children object"))
            obj.ExpandArray = showElement
            obj.configLinkProperty(ShowElement='ExpandArray')
            obj.removeProperty('ShowElement')
        else:
            obj.configLinkProperty(ShowElement='ExpandArray')
        if getattr(obj,'ExpandArray',False):
            obj.setPropertyStatus('PlacementList','Immutable')
        else:
            obj.setPropertyStatus('PlacementList','-Immutable')
        if not hasattr(obj,'LinkTransform'):
            obj.addProperty('App::PropertyBool','LinkTransform',' Link')
        if not hasattr(obj,'ColoredElements'):
            obj.addProperty('App::PropertyLinkSubHidden','ColoredElements',' Link')
            obj.setPropertyStatus('ColoredElements','Hidden')
        obj.configLinkProperty('LinkTransform','ColoredElements')

    def getViewProviderName(self,_obj):
        if self.use_link:
            return 'Gui::ViewProviderLinkPython'
        return ''

    def migrate_attributes(self, obj):
        """Migrate old attribute names to new names if they exist.

        This is done to comply with Python guidelines or fix small issues
        in older code.
        """
        if hasattr(self, "useLink"):
            # This is only needed for some models created in 0.19
            # while it was in development. Afterwards,
            # all models should use 'use_link' by default
            # and this won't be run.
            self.use_link = bool(self.useLink)
            FreeCAD.Console.PrintWarning("Migrating 'useLink' to 'use_link', "
                                         "{} ({})\n".format(obj.Label,
                                                            obj.TypeId))
            del self.useLink

    def onDocumentRestored(self, obj):
        self.migrate_attributes(obj)
        if self.use_link:
            self.linkSetup(obj)
        else:
            obj.setPropertyStatus('Shape','-Transient')
        if obj.Shape.isNull():
            if getattr(obj,'PlacementList',None):
                self.buildShape(obj,obj.Placement,obj.PlacementList)
            else:
                self.execute(obj)

    def buildShape(self,obj,pl,pls):
        import Part
        import DraftGeomUtils

        if self.use_link:
            if not getattr(obj,'ExpandArray',True) or obj.Count != len(pls):
                obj.setPropertyStatus('PlacementList','-Immutable')
                obj.PlacementList = pls
                obj.setPropertyStatus('PlacementList','Immutable')
                obj.Count = len(pls)

        if obj.Base:
            shape = Part.getShape(obj.Base)
            if shape.isNull():
                raise RuntimeError("'{}' cannot build shape of '{}'\n".format(
                        obj.Name,obj.Base.Name))
            else:
                shape = shape.copy()
                shape.Placement = FreeCAD.Placement()
                base = []
                for i,pla in enumerate(pls):
                    vis = getattr(obj,'VisibilityList',[])
                    if len(vis)>i and not vis[i]:
                        continue;
                    # 'I' is a prefix for disambiguation when mapping element names
                    base.append(shape.transformed(pla.toMatrix(),op='I{}'.format(i)))
                if getattr(obj,'Fuse',False) and len(base) > 1:
                    obj.Shape = base[0].multiFuse(base[1:]).removeSplitter()
                else:
                    obj.Shape = Part.makeCompound(base)

                if not DraftGeomUtils.isNull(pl):
                    obj.Placement = pl

        if self.use_link:
            return False # return False to call LinkExtension::execute()

    def onChanged(self, obj, prop):
        if not getattr(self,'use_link',False):
            return
        if prop == 'Fuse':
            if obj.Fuse:
                obj.setPropertyStatus('Shape','-Transient')
            else:
                obj.setPropertyStatus('Shape','Transient')
        elif prop == 'ExpandArray':
            if hasattr(obj,'PlacementList'):
                obj.setPropertyStatus('PlacementList',
                        '-Immutable' if obj.ExpandArray else 'Immutable')

class _Array(_DraftLink):
    "The Draft Array object"

    def __init__(self,obj):
        _DraftLink.__init__(self,obj,"Array")

    def attach(self, obj):
        obj.addProperty("App::PropertyLink","Base","Draft",QT_TRANSLATE_NOOP("App::Property","The base object that must be duplicated"))
        obj.addProperty("App::PropertyEnumeration","ArrayType","Draft",QT_TRANSLATE_NOOP("App::Property","The type of array to create"))
        obj.addProperty("App::PropertyLinkGlobal","AxisReference","Draft",QT_TRANSLATE_NOOP("App::Property","The axis (e.g. DatumLine) overriding Axis/Center"))
        obj.addProperty("App::PropertyVector","Axis","Draft",QT_TRANSLATE_NOOP("App::Property","The axis direction"))
        obj.addProperty("App::PropertyInteger","NumberX","Draft",QT_TRANSLATE_NOOP("App::Property","Number of copies in X direction"))
        obj.addProperty("App::PropertyInteger","NumberY","Draft",QT_TRANSLATE_NOOP("App::Property","Number of copies in Y direction"))
        obj.addProperty("App::PropertyInteger","NumberZ","Draft",QT_TRANSLATE_NOOP("App::Property","Number of copies in Z direction"))
        obj.addProperty("App::PropertyInteger","NumberPolar","Draft",QT_TRANSLATE_NOOP("App::Property","Number of copies"))
        obj.addProperty("App::PropertyVectorDistance","IntervalX","Draft",QT_TRANSLATE_NOOP("App::Property","Distance and orientation of intervals in X direction"))
        obj.addProperty("App::PropertyVectorDistance","IntervalY","Draft",QT_TRANSLATE_NOOP("App::Property","Distance and orientation of intervals in Y direction"))
        obj.addProperty("App::PropertyVectorDistance","IntervalZ","Draft",QT_TRANSLATE_NOOP("App::Property","Distance and orientation of intervals in Z direction"))
        obj.addProperty("App::PropertyVectorDistance","IntervalAxis","Draft",QT_TRANSLATE_NOOP("App::Property","Distance and orientation of intervals in Axis direction"))
        obj.addProperty("App::PropertyVectorDistance","Center","Draft",QT_TRANSLATE_NOOP("App::Property","Center point"))
        obj.addProperty("App::PropertyAngle","Angle","Draft",QT_TRANSLATE_NOOP("App::Property","Angle to cover with copies"))
        obj.addProperty("App::PropertyDistance","RadialDistance","Draft",QT_TRANSLATE_NOOP("App::Property","Distance between copies in a circle"))
        obj.addProperty("App::PropertyDistance","TangentialDistance","Draft",QT_TRANSLATE_NOOP("App::Property","Distance between circles"))
        obj.addProperty("App::PropertyInteger","NumberCircles","Draft",QT_TRANSLATE_NOOP("App::Property","number of circles"))
        obj.addProperty("App::PropertyInteger","Symmetry","Draft",QT_TRANSLATE_NOOP("App::Property","number of circles"))
        obj.addProperty("App::PropertyBool","Fuse","Draft",QT_TRANSLATE_NOOP("App::Property","Specifies if copies must be fused (slower)"))
        obj.Fuse = False
        if self.use_link:
            obj.addProperty("App::PropertyInteger","Count","Draft",'')
            obj.addProperty("App::PropertyBool","ExpandArray","Draft",
                    QT_TRANSLATE_NOOP("App::Property","Show array element as children object"))
            obj.ExpandArray = False

        obj.ArrayType = ['ortho','polar','circular']
        obj.NumberX = 1
        obj.NumberY = 1
        obj.NumberZ = 1
        obj.NumberPolar = 1
        obj.IntervalX = Vector(1,0,0)
        obj.IntervalY = Vector(0,1,0)
        obj.IntervalZ = Vector(0,0,1)
        obj.Angle = 360
        obj.Axis = Vector(0,0,1)
        obj.RadialDistance = 1.0
        obj.TangentialDistance = 1.0
        obj.NumberCircles = 2
        obj.Symmetry = 1

        _DraftLink.attach(self,obj)

    def linkSetup(self,obj):
        _DraftLink.linkSetup(self,obj)
        obj.configLinkProperty(ElementCount='Count')
        obj.setPropertyStatus('Count','Hidden')

    def onChanged(self,obj,prop):
        _DraftLink.onChanged(self,obj,prop)
        if prop == "AxisReference":
            if obj.AxisReference:
                obj.setEditorMode("Center", 1)
                obj.setEditorMode("Axis", 1)
            else:
                obj.setEditorMode("Center", 0)
                obj.setEditorMode("Axis", 0)

    def execute(self,obj):
        if obj.Base:
            pl = obj.Placement
            axis = obj.Axis
            center = obj.Center
            if hasattr(obj,"AxisReference") and obj.AxisReference:
                if hasattr(obj.AxisReference,"Placement"):
                    axis = obj.AxisReference.Placement.Rotation * Vector(0,0,1)
                    center = obj.AxisReference.Placement.Base
                else:
                    raise TypeError("AxisReference has no Placement attribute. Please select a different AxisReference.")
            if obj.ArrayType == "ortho":
                pls = self.rectArray(obj.Base.Placement,obj.IntervalX,obj.IntervalY,
                                    obj.IntervalZ,obj.NumberX,obj.NumberY,obj.NumberZ)
            elif obj.ArrayType == "circular":
                pls = self.circArray(obj.Base.Placement,obj.RadialDistance,obj.TangentialDistance,
                                     axis,center,obj.NumberCircles,obj.Symmetry)
            else:
                av = obj.IntervalAxis if hasattr(obj,"IntervalAxis") else None
                pls = self.polarArray(obj.Base.Placement,center,obj.Angle.Value,obj.NumberPolar,axis,av)

            return _DraftLink.buildShape(self,obj,pl,pls)

    def rectArray(self,pl,xvector,yvector,zvector,xnum,ynum,znum):
        import Part
        base = [pl.copy()]
        for xcount in range(xnum):
            currentxvector=Vector(xvector).multiply(xcount)
            if not xcount==0:
                npl = pl.copy()
                npl.translate(currentxvector)
                base.append(npl)
            for ycount in range(ynum):
                currentyvector=FreeCAD.Vector(currentxvector)
                currentyvector=currentyvector.add(Vector(yvector).multiply(ycount))
                if not ycount==0:
                    npl = pl.copy()
                    npl.translate(currentyvector)
                    base.append(npl)
                for zcount in range(znum):
                    currentzvector=FreeCAD.Vector(currentyvector)
                    currentzvector=currentzvector.add(Vector(zvector).multiply(zcount))
                    if not zcount==0:
                        npl = pl.copy()
                        npl.translate(currentzvector)
                        base.append(npl)
        return base

    def circArray(self,pl,rdist,tdist,axis,center,cnum,sym):
        import Part
        sym = max(1, sym)
        lead = (0,1,0)
        if axis.x == 0 and axis.z == 0: lead = (1,0,0)
        direction = axis.cross(Vector(lead)).normalize()
        base = [pl.copy()]
        for xcount in range(1, cnum):
            rc = xcount*rdist
            c = 2*rc*math.pi
            n = math.floor(c/tdist)
            n = int(math.floor(n/sym)*sym)
            if n == 0: continue
            angle = 360.0/n
            for ycount in range(0, n):
                npl = pl.copy()
                trans = FreeCAD.Vector(direction).multiply(rc)
                npl.translate(trans)
                npl.rotate(npl.Rotation.inverted().multVec(center-trans), axis, ycount*angle)
                base.append(npl)
        return base

    def polarArray(self,spl,center,angle,num,axis,axisvector):
        #print("angle ",angle," num ",num)
        import Part
        spin = FreeCAD.Placement(Vector(), spl.Rotation)
        pl = FreeCAD.Placement(spl.Base, FreeCAD.Rotation())
        center = center.sub(spl.Base)
        base = [spl.copy()]
        if angle == 360:
            fraction = float(angle)/num
        else:
            if num == 0:
                return base
            fraction = float(angle)/(num-1)
        ctr = DraftVecUtils.tup(center)
        axs = DraftVecUtils.tup(axis)
        for i in range(num-1):
            currangle = fraction + (i*fraction)
            npl = pl.copy()
            npl.rotate(ctr, axs, currangle)
            npl = npl.multiply(spin)
            if axisvector:
                if not DraftVecUtils.isNull(axisvector):
                    npl.translate(FreeCAD.Vector(axisvector).multiply(i+1))
            base.append(npl)
        return base

class _ViewProviderDraftLink:
    "a view provider for link type object"

    def __init__(self,vobj):
        self.Object = vobj.Object
        vobj.Proxy = self

    def attach(self,vobj):
        self.Object = vobj.Object

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None

    def getIcon(self):
        tp = self.Object.Proxy.Type
        if tp == 'Array':
            if self.Object.ArrayType == 'ortho':
                return ":/icons/Draft_LinkArray.svg"
            elif self.Object.ArrayType == 'polar':
                return ":/icons/Draft_PolarLinkArray.svg"
            elif self.Object.ArrayType == 'circular':
                return ":/icons/Draft_CircularLinkArray.svg"
        elif tp == 'PathArray':
            return ":/icons/Draft_PathLinkArray.svg"

    def claimChildren(self):
        obj = self.Object
        if hasattr(obj,'ExpandArray'):
            expand = obj.ExpandArray
        else:
            expand = obj.ShowElement
        if not expand:
            return [obj.Base]
        else:
            return obj.ElementList

class _ViewProviderDraftArray(_ViewProviderDraft):
    """a view provider that displays a Array icon instead of a Draft icon"""

    def __init__(self,vobj):
        _ViewProviderDraft.__init__(self,vobj)

    def getIcon(self):
        if hasattr(self.Object, "ArrayType"):
            if self.Object.ArrayType == 'ortho':
                return ":/icons/Draft_Array.svg"
            elif self.Object.ArrayType == 'polar':
                return ":/icons/Draft_PolarArray.svg"
            elif self.Object.ArrayType == 'circular':
                return ":/icons/Draft_CircularArray.svg"
        elif hasattr(self.Object, "PointList"):
            return ":/icons/Draft_PointArray.svg"
        else:
            return ":/icons/Draft_PathArray.svg"

    def resetColors(self, vobj):
        colors = []
        if vobj.Object.Base:
            if vobj.Object.Base.isDerivedFrom("Part::Feature"):
                if len(vobj.Object.Base.ViewObject.DiffuseColor) > 1:
                    colors = vobj.Object.Base.ViewObject.DiffuseColor
                else:
                    c = vobj.Object.Base.ViewObject.ShapeColor
                    c = (c[0],c[1],c[2],vobj.Object.Base.ViewObject.Transparency/100.0)
                    for f in vobj.Object.Base.Shape.Faces:
                        colors.append(c)
        if colors:
            n = 1
            if hasattr(vobj.Object,"ArrayType"):
                if vobj.Object.ArrayType == "ortho":
                    n = vobj.Object.NumberX * vobj.Object.NumberY * vobj.Object.NumberZ
                else:
                    n = vobj.Object.NumberPolar
            elif hasattr(vobj.Object,"Count"):
                n = vobj.Object.Count
            colors = colors * n
            vobj.DiffuseColor = colors

def move(objectslist,vector,copy=False):
    """move(objects,vector,[copy]): Moves the objects contained
    in objects (that can be an object or a list of objects)
    in the direction and distance indicated by the given
    vector. If copy is True, the actual objects are not moved, but copies
    are created instead. The objects (or their copies) are returned."""
    typecheck([(vector,Vector), (copy,bool)], "move")
    if not isinstance(objectslist,list): objectslist = [objectslist]
    objectslist.extend(getMovableChildren(objectslist))
    newobjlist = []
    newgroups = {}
    objectslist = filterObjectsForModifiers(objectslist, copy)
    for obj in objectslist:
        newobj = None
        # real_vector have been introduced to take into account
        # the possibility that object is inside an App::Part
        if hasattr(obj, "getGlobalPlacement"):
            v_minus_global = obj.getGlobalPlacement().inverse().Rotation.multVec(vector)
            real_vector = obj.Placement.Rotation.multVec(v_minus_global)
        else:
            real_vector = vector
        if getType(obj) == "Point":
            v = Vector(obj.X,obj.Y,obj.Z)
            v = v.add(real_vector)
            if copy:
                newobj = makeCopy(obj)
            else:
                newobj = obj
            newobj.X = v.x
            newobj.Y = v.y
            newobj.Z = v.z
        elif obj.isDerivedFrom("App::DocumentObjectGroup"):
            pass
        elif hasattr(obj,'Shape'):
            if copy:
                newobj = makeCopy(obj)
            else:
                newobj = obj
            pla = newobj.Placement
            pla.move(real_vector)
        elif getType(obj) == "Annotation":
            if copy:
                newobj = FreeCAD.ActiveDocument.addObject("App::Annotation",getRealName(obj.Name))
                newobj.LabelText = obj.LabelText
                if gui:
                    formatObject(newobj,obj)
            else:
                newobj = obj
            newobj.Position = obj.Position.add(real_vector)
        elif getType(obj) == "DraftText":
            if copy:
                newobj = FreeCAD.ActiveDocument.addObject("App::FeaturePython",getRealName(obj.Name))
                DraftText(newobj)
                if gui:
                    ViewProviderDraftText(newobj.ViewObject)
                    formatObject(newobj,obj)
                newobj.Text = obj.Text
                newobj.Placement = obj.Placement
                if gui:
                    formatObject(newobj,obj)
            else:
                newobj = obj
            newobj.Placement.Base = obj.Placement.Base.add(real_vector)
        elif getType(obj) in ["Dimension","LinearDimension"]:
            if copy:
                newobj = FreeCAD.ActiveDocument.addObject("App::FeaturePython",getRealName(obj.Name))
                _Dimension(newobj)
                if gui:
                    _ViewProviderDimension(newobj.ViewObject)
                    formatObject(newobj,obj)
            else:
                newobj = obj
            newobj.Start = obj.Start.add(real_vector)
            newobj.End = obj.End.add(real_vector)
            newobj.Dimline = obj.Dimline.add(real_vector)
        else:
            if copy and obj.isDerivedFrom("Mesh::Feature"):
                print("Mesh copy not supported at the moment") # TODO
            newobj = obj
            if "Placement" in obj.PropertiesList:
                pla = obj.Placement
                pla.move(real_vector)
        if newobj is not None:
            newobjlist.append(newobj)
        if copy:
            for p in obj.InList:
                if p.isDerivedFrom("App::DocumentObjectGroup") and (p in objectslist):
                    g = newgroups.setdefault(p.Name,FreeCAD.ActiveDocument.addObject(p.TypeId,p.Name))
                    g.addObject(newobj)
                    break
                if getType(p) == "Layer":
                    p.Proxy.addObject(p,newobj)
    if copy and getParam("selectBaseObjects",False):
        select(objectslist)
    else:
        select(newobjlist)
    if len(newobjlist) == 1: return newobjlist[0]
    return newobjlist

def rotate(objectslist,angle,center=Vector(0,0,0),axis=Vector(0,0,1),copy=False):
    """rotate(objects,angle,[center,axis,copy]): Rotates the objects contained
    in objects (that can be a list of objects or an object) of the given angle
    (in degrees) around the center, using axis as a rotation axis. If axis is
    omitted, the rotation will be around the vertical Z axis.
    If copy is True, the actual objects are not moved, but copies
    are created instead. The objects (or their copies) are returned."""
    import Part
    typecheck([(copy,bool)], "rotate")
    if not isinstance(objectslist,list): objectslist = [objectslist]
    objectslist.extend(getMovableChildren(objectslist))
    newobjlist = []
    newgroups = {}
    objectslist = filterObjectsForModifiers(objectslist, copy)
    for obj in objectslist:
        newobj = None
        # real_center and real_axis are introduced to take into account
        # the possibility that object is inside an App::Part
        if hasattr(obj, "getGlobalPlacement"):
            ci = obj.getGlobalPlacement().inverse().multVec(center)
            real_center = obj.Placement.multVec(ci)
            ai = obj.getGlobalPlacement().inverse().Rotation.multVec(axis)
            real_axis = obj.Placement.Rotation.multVec(ai)
        else:
            real_center = center
            real_axis = axis

        if copy:
            newobj = makeCopy(obj)
        else:
            newobj = obj
        if obj.isDerivedFrom("App::Annotation"):
            if axis.normalize() == Vector(1,0,0):
                newobj.ViewObject.RotationAxis = "X"
                newobj.ViewObject.Rotation = angle
            elif axis.normalize() == Vector(0,1,0):
                newobj.ViewObject.RotationAxis = "Y"
                newobj.ViewObject.Rotation = angle
            elif axis.normalize() == Vector(0,-1,0):
                newobj.ViewObject.RotationAxis = "Y"
                newobj.ViewObject.Rotation = -angle
            elif axis.normalize() == Vector(0,0,1):
                newobj.ViewObject.RotationAxis = "Z"
                newobj.ViewObject.Rotation = angle
            elif axis.normalize() == Vector(0,0,-1):
                newobj.ViewObject.RotationAxis = "Z"
                newobj.ViewObject.Rotation = -angle
        elif getType(obj) == "Point":
            v = Vector(obj.X,obj.Y,obj.Z)
            rv = v.sub(real_center)
            rv = DraftVecUtils.rotate(rv,math.radians(angle),real_axis)
            v = real_center.add(rv)
            newobj.X = v.x
            newobj.Y = v.y
            newobj.Z = v.z
        elif obj.isDerivedFrom("App::DocumentObjectGroup"):
            pass
        elif hasattr(obj,"Placement"):
            #FreeCAD.Console.PrintMessage("placement rotation\n")
            shape = Part.Shape()
            shape.Placement = obj.Placement
            shape.rotate(DraftVecUtils.tup(real_center), DraftVecUtils.tup(real_axis), angle)
            newobj.Placement = shape.Placement
        elif hasattr(obj,'Shape') and (getType(obj) not in ["WorkingPlaneProxy","BuildingPart"]):
            #think it make more sense to try first to rotate placement and later to try with shape. no?
            shape = obj.Shape.copy()
            shape.rotate(DraftVecUtils.tup(real_center), DraftVecUtils.tup(real_axis), angle)
            newobj.Shape = shape
        if copy:
            formatObject(newobj,obj)
        if newobj is not None:
            newobjlist.append(newobj)
        if copy:
            for p in obj.InList:
                if p.isDerivedFrom("App::DocumentObjectGroup") and (p in objectslist):
                    g = newgroups.setdefault(p.Name,FreeCAD.ActiveDocument.addObject(p.TypeId,p.Name))
                    g.addObject(newobj)
                    break
    if copy and getParam("selectBaseObjects",False):
        select(objectslist)
    else:
        select(newobjlist)
    if len(newobjlist) == 1: return newobjlist[0]
    return newobjlist

def makeCopy(obj,force=None,reparent=False):
    """makeCopy(object): returns an exact copy of an object"""
    if not FreeCAD.ActiveDocument:
        FreeCAD.Console.PrintError("No active document. Aborting\n")
        return
    if (getType(obj) == "Rectangle") or (force == "Rectangle"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _Rectangle(newobj)
        if gui:
            _ViewProviderRectangle(newobj.ViewObject)
    elif (getType(obj) == "Point") or (force == "Point"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _Point(newobj)
        if gui:
            _ViewProviderPoint(newobj.ViewObject)
    elif (getType(obj) in ["Dimension","LinearDimension"]) or (force == "Dimension"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _Dimension(newobj)
        if gui:
            _ViewProviderDimension(newobj.ViewObject)
    elif (getType(obj) == "Wire") or (force == "Wire"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _Wire(newobj)
        if gui:
            _ViewProviderWire(newobj.ViewObject)
    elif (getType(obj) == "Circle") or (force == "Circle"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _Circle(newobj)
        if gui:
            _ViewProviderDraft(newobj.ViewObject)
    elif (getType(obj) == "Polygon") or (force == "Polygon"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _Polygon(newobj)
        if gui:
            _ViewProviderDraft(newobj.ViewObject)
    elif (getType(obj) == "BSpline") or (force == "BSpline"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _BSpline(newobj)
        if gui:
            _ViewProviderWire(newobj.ViewObject)
    elif (getType(obj) == "Block") or (force == "BSpline"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _Block(newobj)
        if gui:
            _ViewProviderDraftPart(newobj.ViewObject)
    elif (getType(obj) == "DrawingView") or (force == "DrawingView"):
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        _DrawingView(newobj)
    elif (getType(obj) == "Structure") or (force == "Structure"):
        import ArchStructure
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        ArchStructure._Structure(newobj)
        if gui:
            ArchStructure._ViewProviderStructure(newobj.ViewObject)
    elif (getType(obj) == "Wall") or (force == "Wall"):
        import ArchWall
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        ArchWall._Wall(newobj)
        if gui:
            ArchWall._ViewProviderWall(newobj.ViewObject)
    elif (getType(obj) == "Window") or (force == "Window"):
        import ArchWindow
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        ArchWindow._Window(newobj)
        if gui:
            ArchWindow._ViewProviderWindow(newobj.ViewObject)
    elif (getType(obj) == "Panel") or (force == "Panel"):
        import ArchPanel
        newobj = FreeCAD.ActiveDocument.addObject(obj.TypeId,getRealName(obj.Name))
        ArchPanel._Panel(newobj)
        if gui:
            ArchPanel._ViewProviderPanel(newobj.ViewObject)
    elif (getType(obj) == "Sketch") or (force == "Sketch"):
        newobj = FreeCAD.ActiveDocument.addObject("Sketcher::SketchObject",getRealName(obj.Name))
        for geo in obj.Geometry:
            newobj.addGeometry(geo)
        for con in obj.Constraints:
            newobj.addConstraint(con)
    elif hasattr(obj, 'Shape'):
        newobj = FreeCAD.ActiveDocument.addObject("Part::Feature",getRealName(obj.Name))
        newobj.Shape = obj.Shape
    else:
        print("Error: Object type cannot be copied")
        return None
    for p in obj.PropertiesList:
        if not p in ["Proxy","ExpressionEngine"]:
            if p in newobj.PropertiesList:
                if not "ReadOnly" in newobj.getEditorMode(p):
                    try:
                        setattr(newobj,p,obj.getPropertyByName(p))
                    except AttributeError:
                        try:
                            setattr(newobj,p,obj.getPropertyByName(p).Value)
                        except AttributeError:
                            pass
    if reparent:
        parents = obj.InList
        if parents:
            for par in parents:
                if par.isDerivedFrom("App::DocumentObjectGroup"):
                    par.addObject(newobj)
                else:
                    for prop in par.PropertiesList:
                        if getattr(par,prop) == obj:
                            setattr(par,prop,newobj)

    formatObject(newobj,obj)
    return newobj

def filterObjectsForModifiers(objects, isCopied=False):
    filteredObjects = []
    for object in objects:
        if hasattr(object, "MoveBase") and object.MoveBase and object.Base:
            parents = []
            for parent in object.Base.InList:
                if parent.isDerivedFrom("Part::Feature"):
                    parents.append(parent.Name)
            if len(parents) > 1:
                warningMessage = translate("draft","%s shares a base with %d other objects. Please check if you want to modify this.") % (object.Name,len(parents) - 1)
                FreeCAD.Console.PrintError(warningMessage)
                if FreeCAD.GuiUp:
                    FreeCADGui.getMainWindow().showMessage(warningMessage, 0)
            filteredObjects.append(object.Base)
        elif hasattr(object,"Placement") and object.getEditorMode("Placement") == ["ReadOnly"] and not isCopied:
           FreeCAD.Console.PrintError(translate("Draft","%s cannot be modified because its placement is readonly.") % obj.Name)
           continue
        else:
           filteredObjects.append(object)
    return filteredObjects

import getSVG as svg


getSVG = svg.getSVG

def getDXF(obj,direction=None):
    """getDXF(object,[direction]): returns a DXF entity from the given
    object. If direction is given, the object is projected in 2D."""
    plane = None
    result = ""
    if obj.isDerivedFrom("Drawing::View") or obj.isDerivedFrom("TechDraw::DrawView"):
        if obj.Source.isDerivedFrom("App::DocumentObjectGroup"):
            for o in obj.Source.Group:
                result += getDXF(o,obj.Direction)
        else:
            result += getDXF(obj.Source,obj.Direction)
        return result
    if direction:
        if isinstance(direction,FreeCAD.Vector):
            if direction != Vector(0,0,0):
                plane = WorkingPlane.plane()
                plane.alignToPointAndAxis(Vector(0,0,0),direction)

    def getProj(vec):
        if not plane: return vec
        nx = DraftVecUtils.project(vec,plane.u)
        ny = DraftVecUtils.project(vec,plane.v)
        return Vector(nx.Length,ny.Length,0)

    if getType(obj) in ["Dimension","LinearDimension"]:
        p1 = getProj(obj.Start)
        p2 = getProj(obj.End)
        p3 = getProj(obj.Dimline)
        result += "0\nDIMENSION\n8\n0\n62\n0\n3\nStandard\n70\n1\n"
        result += "10\n"+str(p3.x)+"\n20\n"+str(p3.y)+"\n30\n"+str(p3.z)+"\n"
        result += "13\n"+str(p1.x)+"\n23\n"+str(p1.y)+"\n33\n"+str(p1.z)+"\n"
        result += "14\n"+str(p2.x)+"\n24\n"+str(p2.y)+"\n34\n"+str(p2.z)+"\n"

    elif getType(obj) == "Annotation":
        p = getProj(obj.Position)
        count = 0
        for t in obj.LabeLtext:
            result += "0\nTEXT\n8\n0\n62\n0\n"
            result += "10\n"+str(p.x)+"\n20\n"+str(p.y+count)+"\n30\n"+str(p.z)+"\n"
            result += "40\n1\n"
            result += "1\n"+str(t)+"\n"
            result += "7\nSTANDARD\n"
            count += 1

    elif hasattr(obj,'Shape'):
        # TODO do this the Draft way, for ex. using polylines and rectangles
        import Drawing
        if not direction:
            direction = FreeCAD.Vector(0,0,-1)
        if DraftVecUtils.isNull(direction):
            direction = FreeCAD.Vector(0,0,-1)
        try:
            d = Drawing.projectToDXF(obj.Shape,direction)
        except:
            print("Draft.getDXF: Unable to project ",obj.Label," to ",direction)
        else:
            result += d

    else:
        print("Draft.getDXF: Unsupported object: ",obj.Label)

    return result

class _DrawingView(_DraftObject):
    """The Draft DrawingView object"""
    def __init__(self, obj):
        _DraftObject.__init__(self,obj,"DrawingView")
        obj.addProperty("App::PropertyVector","Direction","Shape View",QT_TRANSLATE_NOOP("App::Property","Projection direction"))
        obj.addProperty("App::PropertyFloat","LineWidth","View Style",QT_TRANSLATE_NOOP("App::Property","The width of the lines inside this object"))
        obj.addProperty("App::PropertyLength","FontSize","View Style",QT_TRANSLATE_NOOP("App::Property","The size of the texts inside this object"))
        obj.addProperty("App::PropertyLength","LineSpacing","View Style",QT_TRANSLATE_NOOP("App::Property","The spacing between lines of text"))
        obj.addProperty("App::PropertyColor","LineColor","View Style",QT_TRANSLATE_NOOP("App::Property","The color of the projected objects"))
        obj.addProperty("App::PropertyLink","Source","Base",QT_TRANSLATE_NOOP("App::Property","The linked object"))
        obj.addProperty("App::PropertyEnumeration","FillStyle","View Style",QT_TRANSLATE_NOOP("App::Property","Shape Fill Style"))
        obj.addProperty("App::PropertyEnumeration","LineStyle","View Style",QT_TRANSLATE_NOOP("App::Property","Line Style"))
        obj.addProperty("App::PropertyBool","AlwaysOn","View Style",QT_TRANSLATE_NOOP("App::Property","If checked, source objects are displayed regardless of being visible in the 3D model"))
        obj.FillStyle = ['shape color'] + list(svgpatterns().keys())
        obj.LineStyle = ['Solid','Dashed','Dotted','Dashdot']
        obj.LineWidth = 0.35
        obj.FontSize = 12

    def execute(self, obj):
        result = ""
        if hasattr(obj,"Source"):
            if obj.Source:
                if hasattr(obj,"LineStyle"):
                    ls = obj.LineStyle
                else:
                    ls = None
                if hasattr(obj,"LineColor"):
                    lc = obj.LineColor
                else:
                    lc = None
                if hasattr(obj,"LineSpacing"):
                    lp = obj.LineSpacing
                else:
                    lp = None
                if obj.Source.isDerivedFrom("App::DocumentObjectGroup"):
                    svg = ""
                    shapes = []
                    others = []
                    objs = getGroupContents([obj.Source])
                    for o in objs:
                        v = o.ViewObject.isVisible()
                        if hasattr(obj,"AlwaysOn"):
                            if obj.AlwaysOn:
                                v = True
                        if v:
                            svg += getSVG(o,obj.Scale,obj.LineWidth,obj.FontSize.Value,obj.FillStyle,obj.Direction,ls,lc,lp)
                else:
                    svg = getSVG(obj.Source,obj.Scale,obj.LineWidth,obj.FontSize.Value,obj.FillStyle,obj.Direction,ls,lc,lp)
                result += '<g id="' + obj.Name + '"'
                result += ' transform="'
                result += 'rotate('+str(obj.Rotation)+','+str(obj.X)+','+str(obj.Y)+') '
                result += 'translate('+str(obj.X)+','+str(obj.Y)+') '
                result += 'scale('+str(obj.Scale)+','+str(-obj.Scale)+')'
                result += '">'
                result += svg
                result += '</g>'
        obj.ViewResult = result

    def getDXF(self,obj):
        "returns a DXF fragment"
        return getDXF(obj)
