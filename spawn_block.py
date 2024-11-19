import unreal

def create_cube(x, y, z, w, name="cube"):

    # Creare un attore di tipo StaticMeshActor
    actor_location = unreal.Vector(x, y, z)
    static_mesh_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor, actor_location)

    # Assegnare una mesh al nostro attore
    static_mesh_component = static_mesh_actor.static_mesh_component
    cube_mesh = unreal.EditorAssetLibrary.load_asset('/Engine/BasicShapes/Cube.Cube')
    static_mesh_component.set_static_mesh(cube_mesh)

    # Impostare la scala del cubo 
    static_mesh_component.set_world_scale3d(unreal.Vector(w, w, w))
    static_mesh_actor.set_actor_label(name)


locations = [
    [535.6, 103.4, 939.6], # pollice sx
    [-545.7, 127.7, 932.2], # pollice dx
    [67, 54, 1243], # clavicola sx
    [-73, 54, 1243], # clavicola dx
]

for loc in locations:
    x, y, z = loc
    create_cube(x, y, z, 0.1, name=f"cube_{x:.0f}_{y:.0f}_{z:.0f}")




1568
