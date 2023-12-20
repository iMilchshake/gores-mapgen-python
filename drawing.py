import dearpygui.dearpygui as dpg

COLOR_BORDER_OUT = (125, 125, 125)
COLOR_BORDER_IN = COLOR_BORDER_OUT
INPUT_WIDTH = 150


def draw_grid():
    # fetch configuration
    cells_x = dpg.get_value('cells_x')
    cells_y = dpg.get_value('cells_y')
    border_size = dpg.get_value('border_size')
    cell_size = dpg.get_value('cell_size')

    # initialize or prepare canvas for (re)drawing
    size_x = cells_x * cell_size + (cells_x + 1) * border_size
    size_y = cells_y * cell_size + (cells_y + 1) * border_size
    if dpg.does_item_exist('canvas'):
        dpg.configure_item('canvas', width=size_x, height=size_y)
        dpg.delete_item('canvas', children_only=True)
    else:
        dpg.add_drawlist(size_x, size_y, tag='canvas')

    # Draw borders
    for x in range(0, size_x, cell_size + border_size):
        dpg.draw_rectangle((x, 0), (x + border_size, size_y),
                           color=COLOR_BORDER_OUT, fill=COLOR_BORDER_IN, parent='canvas')
    for y in range(0, size_y, cell_size + border_size):
        dpg.draw_rectangle((0, y), (size_x, y + border_size),
                           color=COLOR_BORDER_OUT, fill=COLOR_BORDER_IN, parent='canvas')

    # Draw cells
    for x in range(cells_x):
        for y in range(cells_y):
            cell_x1 = x * (cell_size + border_size) + border_size
            cell_y1 = y * (cell_size + border_size) + border_size
            cell_x2 = cell_x1 + cell_size
            cell_y2 = cell_y1 + cell_size
            dpg.draw_rectangle((cell_x1, cell_y1), (cell_x2, cell_y2),
                               color=(255, 0, 0), parent='canvas')

    print(dpg.get_item_configuration('window'))


dpg.create_context()

with dpg.value_registry():
    dpg.add_int_value(default_value=10, tag="cells_x")
    dpg.add_int_value(default_value=10, tag="cells_y")
    dpg.add_int_value(default_value=5, tag="border_size")
    dpg.add_int_value(default_value=25, tag="cell_size")

with dpg.window(label="Grid visualizer", tag='window', autosize=True):
    draw_grid()
    dpg.add_separator()
    dpg.add_input_int(label='cells_x', source='cells_x', width=INPUT_WIDTH, callback=draw_grid)
    dpg.add_input_int(label='cells_y', source='cells_y', width=INPUT_WIDTH, callback=draw_grid)
    dpg.add_input_int(label='border_size', source='border_size', width=INPUT_WIDTH, callback=draw_grid)
    dpg.add_input_int(label='cell_size', source='cell_size', width=INPUT_WIDTH, callback=draw_grid)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.show_metrics()
dpg.start_dearpygui()
dpg.destroy_context()
