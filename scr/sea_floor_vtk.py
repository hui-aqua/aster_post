import vtk
import numpy as np
import os

def out_put(boundry,water_depth,output_floder=False):

    Points = vtk.vtkPoints()
    Triangles = vtk.vtkCellArray()
    one_tri = vtk.vtkTriangle()
     # sea floor
    bound=boundry
    floot_point=[[ bound, bound,-water_depth],
                 [ bound,-bound,-water_depth],
                 [-bound,-bound,-water_depth],
                 [-bound, bound,-water_depth],]
    for each in floot_point:
        Points.InsertNextPoint(each)
    one_tri.GetPointIds().SetId(0, 0)
    one_tri.GetPointIds().SetId(1, 1)
    one_tri.GetPointIds().SetId(2, 2)
    Triangles.InsertNextCell(one_tri)
    one_tri.GetPointIds().SetId(0, 2)
    one_tri.GetPointIds().SetId(1, 3)
    one_tri.GetPointIds().SetId(2, 0)
    Triangles.InsertNextCell(one_tri)
    # out put data
    out_data = vtk.vtkPolyData()
    out_data.SetPoints(Points)
    out_data.SetPolys(Triangles)
    out_data.Modified()
    if vtk.VTK_MAJOR_VERSION <= 5:
        out_data.Update()
    writer = vtk.vtkXMLPolyDataWriter();
    if output_floder is not False:
        writer.SetFileName(os.path.join(output_floder,"seaFloor.vtp"))
    else:
        writer.SetFileName("post_data/seaFloor.vtp");
    if vtk.VTK_MAJOR_VERSION <= 5:
        writer.SetInput(out_data)
    else:
        writer.SetInputData(out_data)
    writer.Write()

if __name__ == "__main__":
    water_depth=60
    boundry=200
    out_put(boundry,water_depth)