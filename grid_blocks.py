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


volume_bounds = {
    "x": [-230, +230],
    "y": [15, 260],
    "z": [10, 1260],
}

n_steps_xyz = [3, 3, 7]

x_step = (volume_bounds["x"][1] - volume_bounds["x"][0]) / (n_steps_xyz[0]-1)
y_step = (volume_bounds["y"][1] - volume_bounds["y"][0]) / (n_steps_xyz[1]-1)
z_step = (volume_bounds["z"][1] - volume_bounds["z"][0]) / (n_steps_xyz[2]-1)

x_locations = [volume_bounds["x"][0] + x_step*(i) for i in range(n_steps_xyz[0])]
y_locations = [volume_bounds["y"][0] + y_step*(i) for i in range(n_steps_xyz[1])]
z_locations = [volume_bounds["z"][0] + z_step*(i) for i in range(n_steps_xyz[2])]

for z in z_locations:
    for x in x_locations:
        for y in y_locations:
            #create_cube(x, y, z, 0.1, name=f"cube_{x:.0f}_{y:.0f}_{z:.0f}")
            print(f"[{x:.1f}, {y:.1f}, {z:.1f}],")
