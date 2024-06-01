import os

def find_files_by_cycle_number(directory, cycle_number):
    """
    在指定目录中搜索并返回符合特定周期号的 .nc 文件的完整路径列表。

    参数:
    directory : str
        要搜索的目录的路径。函数将遍历此目录下的所有子文件夹。
    cycle_number : int
        目标周期号，函数将查找以 'cycle_' 开头且后跟周期号的文件夹。

    返回:
    list of str
        匹配的文件路径列表。每个列表项是一个字符串，代表找到的文件的完整路径。
        如果没有找到任何文件，返回一个空列表。

    功能描述:
    该函数首先确保周期号是一个填充至三位数的字符串，然后遍历指定目录下的所有文件夹。
    对于每个文件夹，如果其名称符合 'cycle_<周期号>' 的格式，函数将进一步检查该文件夹内的文件。
    函数筛选出扩展名为 .nc 的文件，并将这些文件的完整路径添加到结果列表中。
    最后，返回包含所有匹配文件路径的列表。

    示例:
    >>> directory = 'D:\\swot\\v1.0\\Basic'
    >>> cycle_number = 2
    >>> find_files_by_cycle_number(directory, cycle_name)
    ['D:\\swot\\v1.0\\Basic\\cycle_002\\file1.nc', 'D:\\swot\\v1.0\\Basic\\cycle_002\\file2.nc']
    """
    matching_files = []
    cycle_number_str = str(cycle_number).zfill(3)
    for folder in os.listdir(directory):
        if folder.startswith(f'cycle_{cycle_number_str}'):
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path):
                for filename in os.listdir(folder_path):
                    if filename.endswith('.nc'):
                        full_path = os.path.join(folder_path, filename)
                        matching_files.append(full_path)
    return matching_files

def calculate_orbit_number(input_number):
    """
    Calculate the transformed orbit number.

    This function transforms the input orbit number by subtracting 253, then ensures the
    result is within the valid range of 1 to 589 by looping around using modulo operation.

    Parameters:
    input_number (int): The original orbit number.

    Returns:
    int: The transformed orbit number, correctly looped within range.
    # Example usage to check specific cases
    print("Transformed orbit for 141 should be 472:", calculate_orbit_number(141))
    print("Transformed orbit for 254 should be 1:", calculate_orbit_number(254))

    """
    total_orbits = 584
    # Transform the orbit number by subtracting 253
    transformed_number = input_number - 253
    # Loop back within the range of 1 to total_orbits using modulo operation
    transformed_number = (transformed_number - 1) % total_orbits + 1

    return transformed_number


def find_files_with_orbit_number2(directory, orbit_number):
    # 遍历所有目录下的，同一个轨道编号的文件
    matching_files = []
    # 确保轨道编号是字符串格式
    orbit_number_str = str(orbit_number).zfill(3)  # 填充到3位数

    # 遍历指定目录下的所有文件夹
    for folder in os.listdir(directory):
        # 检查文件夹名是否以 'cycle_' 开头并且数字部分大于474
        if folder.startswith('cycle_'):
            cycle_number = int(folder.split('_')[1])
            if cycle_number < 474:
                folder_path = os.path.join(directory, folder)
                if os.path.isdir(folder_path):  # 确保是文件夹
                    # 遍历文件夹内的所有文件
                    for filename in os.listdir(folder_path):
                        if filename.endswith('.nc'):  # 确保文件是.nc格式
                            if filename[25:28] == orbit_number_str:
                                full_path = os.path.join(folder_path, filename)
                                matching_files.append(full_path)

    return matching_files

def find_files_by_cycle_number3(directory, cycle_number):
    # 在一个周期目录中的奇数轨道    
    matching_files = []
    # 确保周期号是字符串格式，并填充至相应的位数，假设周期号至少是三位数
    cycle_number_str = str(cycle_number).zfill(3)

    # 遍历指定目录下的所有文件夹
    for folder in os.listdir(directory):
        # 检查文件夹名是否以 'cycle_' 开头并且数字部分匹配指定的周期号
        if folder.startswith(f'cycle_{cycle_number_str}'):
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path):  # 确保是文件夹
                # 遍历文件夹内的所有文件
                for filename in os.listdir(folder_path):
                    if filename.endswith('.nc'):  # 确保文件是.nc格式
                        # 获取文件名中特定部分，检查是否是数字且为奇数
                        number_part = filename[25:28]
                        if number_part.isdigit() and int(number_part) % 2 != 0:
                            full_path = os.path.join(folder_path, filename)
                            matching_files.append(full_path)

    return matching_files

def find_files_by_cycle_number4(directory, cycle_number):
    # 在一个周期目录中的偶数轨道
    matching_files = []
    # 确保周期号是字符串格式，并填充至相应的位数，假设周期号至少是三位数
    cycle_number_str = str(cycle_number).zfill(3)

    # 遍历指定目录下的所有文件夹
    for folder in os.listdir(directory):
        # 检查文件夹名是否以 'cycle_' 开头并且数字部分匹配指定的周期号
        if folder.startswith(f'cycle_{cycle_number_str}'):
            folder_path = os.path.join(directory, folder)
            if os.path.isdir(folder_path):  # 确保是文件夹
                # 遍历文件夹内的所有文件
                for filename in os.listdir(folder_path):
                    if filename.endswith('.nc'):  # 确保文件是.nc格式
                        # 获取文件名中特定部分，检查是否是数字且为奇数
                        number_part = filename[25:28]
                        if number_part.isdigit() and int(number_part) % 2 == 0:
                            full_path = os.path.join(folder_path, filename)
                            matching_files.append(full_path)

    return matching_files