import unreal

# volume bounds
# "x": [-230, +230],
# "y": [15, 260],
# "z": [10, 1260],

locations_3d = [
    # [-200, 200, 500],
    # [0, 200, 700],
    # [100, 230, 400],
    [260, 300, 1000]
]


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

for loc in locations_3d:
    x, y, z = loc
    create_cube(x, y, z, 0.1, name=f"cube_{x:.0f}_{y:.0f}_{z:.0f}")