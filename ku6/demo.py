def test():
    task_list = []
    for index in range(10):
        task_list.append({'index': index, 'name': 'name' + str(index)})

    # print(task_list)

    return task_list


if __name__ == '__main__':
    new_list = test()
    print(new_list)
    n_list = [item['name'] for item in new_list]

    print(n_list)
