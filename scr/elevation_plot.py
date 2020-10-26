from vtk import *
import numpy as np

eleva=np.loadtxt("elevation_0.4.txt")

Points = vtk.vtkPoints()
Triangles = vtk.vtkCellArray()
one_tri = vtk.vtkTriangle()
# plot the elevation at y=-100 and y=100
for each in eleva:
    Points.InsertNextPoint(each-np.array([0,100,0]))
    Points.InsertNextPoint(each+np.array([0,100,0]))

# generate triangles
for j in range(len(eleva)-10):
    for i in range(3):
        one_tri.GetPointIds().SetId(i, j*2+i)
    Triangles.InsertNextCell(one_tri)  
    for i in range(2):
        one_tri.GetPointIds().SetId(i, (j+1)*2+i)
    one_tri.GetPointIds().SetId(2, (j+1)*2-1)
    Triangles.InsertNextCell(one_tri)  

# sea floor
bound=200
floot_point=[[ bound, bound,-60],
             [ bound,-bound,-60],
             [-bound,-bound,-60],
             [-bound, bound,-60],]
for each in floot_point:
    Points.InsertNextPoint(each)
one_tri.GetPointIds().SetId(0, len(eleva)*2+0)
one_tri.GetPointIds().SetId(1, len(eleva)*2+1)
one_tri.GetPointIds().SetId(2, len(eleva)*2+2)
Triangles.InsertNextCell(one_tri)

one_tri.GetPointIds().SetId(0, len(eleva)*2+2)
one_tri.GetPointIds().SetId(1, len(eleva)*2+3)
one_tri.GetPointIds().SetId(2, len(eleva)*2+0)
Triangles.InsertNextCell(one_tri)



# out put data
out_data = vtk.vtkPolyData()
out_data.SetPoints(Points)
out_data.SetPolys(Triangles)
out_data.Modified()

if vtk.VTK_MAJOR_VERSION <= 5:
    out_data.Update()

writer = vtk.vtkXMLPolyDataWriter();
writer.SetFileName("ele.vtp");
if vtk.VTK_MAJOR_VERSION <= 5:
    writer.SetInput(out_data)
else:
    writer.SetInputData(out_data)
writer.Write()

