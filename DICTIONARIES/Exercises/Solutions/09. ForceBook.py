def add_users(forces_dc, site_to_join, user_to_add):
    for side, users in forces_dc.items():
        if user_to_add in users:
            return forces_dc
    if site_to_join not in forces_dc:
        forces_dc[site_to_join] = []
        forces_dc[site_to_join].append(user_to_add)
    else:
        if user_to_add not in forces_dc[site_to_join]:
            forces_dc[site_to_join].append(user_to_add)
    return forces_dc


def transfer_users(forces_d, site_to_check, user_to_transfer):
    for site, users in forces_d.items():
        if user_to_transfer in users:
            forces_d[site].remove(user_to_transfer)
            return add_users(forces_d, site_to_check, user_to_transfer)

    return add_users(forces_d, site_to_check, user_to_transfer)


data = input()

forces = {}

while not data == "Lumpawaroo":
    command = data.split(" | ")

    if len(command) > 1:
        site, user = data.split(' | ')
        forces = add_users(forces, site, user)
    else:
        user, site = data.split(" -> ")
        forces = transfer_users(forces, site, user)
        print(f"{user} joins the {site} side!")

    data = input()

order_forces = sorted(forces.items(), key=lambda x: (-len(x[1]), x[0]))

for site, users in order_forces:
    if len(users) > 0:
        print(f"Side: {site}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")
