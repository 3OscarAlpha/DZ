# double Disk_radius_points[NUM_OF_DISK_RADIUS_POINTS]; //
# double Disk_height_points[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double ngas_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double gas_temperature_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double dust_temperature_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double abundance_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double H2_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double e_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double dust2gas_mass_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];
# double vturb_matrix[NUM_OF_DISK_RADIUS_POINTS][NUM_OF_DISK_HEIGHT_POINTS];


f = open ('C:/Users/3512/Downloads/the_task_itself/disk_model.dat', 'r')
data = f.readlines()
r, z, n_gas, T_gas, T_dust, H2O_abun, H2_abun, e_abun, dust2gas, dv_turb = [], [], [], [], [], [], [], [], [], []
for line in data:
    r.append(line.split(" ")[0])
    z.append(line.split(" ")[1])
    n_gas.append(line.split(" ")[2])
    T_gas.append(line.split(" ")[3])
    T_dust.append(line.split(" ")[4])
    H2O_abun.append(line.split(" ")[5])
    H2_abun.append(line.split(" ")[6])
    e_abun.append(line.split(" ")[7])
    dust2gas.append(line.split(" ")[8])
    dv_turb.append(line.split(" ")[9])
del r[0:2], z[0:2], n_gas[0:2], T_gas[0:2], T_dust[0:2], H2O_abun[0:2], H2_abun[0:2], e_abun[0:2], dust2gas[0:2], dv_turb[0:2]  #убираю комментарии
Disk_radius_points, Disk_height_points, ngas_matrix, gas_temperature_matrix, dust_temperature_matrix = [], [], [], [], []
abundance_matrix, H2_matrix, e_matrix, dust2gas_mass_matrix, vturb_matrix = [], [], [], [], []
for i in range (0, len(r)):
    if r[i] != r[i-1]:
        Disk_radius_points.append(r[i])
        Disk_height_points.append([])
        ngas_matrix.append([]) , gas_temperature_matrix.append([])
        dust_temperature_matrix.append([]), abundance_matrix.append([]), H2_matrix.append([]), e_matrix.append([])
        dust2gas_mass_matrix.append([]), vturb_matrix.append([])
sum = 0
for i in range(0, len(Disk_radius_points)):
    for j in range(sum, len(r)):
        if Disk_radius_points[i] == r[j]:
            Disk_height_points[i].append(z[j])
            ngas_matrix[i].append(n_gas[j])
            gas_temperature_matrix[i].append(T_gas[j])
            dust_temperature_matrix[i].append(T_dust[j])
            abundance_matrix[i].append(H2O_abun[j])
            H2_matrix[i].append(H2_abun[j])
            e_matrix[i].append(e_abun[j])
            dust2gas_mass_matrix[i].append(dust2gas[j])
            vturb_matrix[i].append(dv_turb[j])
            sum += 1
        else: break
print(Disk_height_points[1][2])
print(len(Disk_radius_points))

