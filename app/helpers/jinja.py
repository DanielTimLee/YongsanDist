from app import app
from app.helpers.api_request import RequestBoardAPI
from app.routes.oauth import get_oauth_url


@app.context_processor
def inject_oauth():
    return {
        'oauth_req_url': get_oauth_url()
    }


board_color_map = dict()
board_name = list()
random_color = ['teal', 'yellow', 'pink', 'blue', 'brown', 'purple', 'olive', 'black', 'violet', 'green', 'grey',
                'orange', 'red']
random_color_len = len(random_color)
board_list = RequestBoardAPI.get_board_list()
for idx in range(0, len(board_list)):
    board_color_map[board_list[idx]['name']] = random_color[int(idx % random_color_len)]


@app.context_processor
def inject_board():
    return {
        'board_list': board_list
    }


@app.add_template_filter
def board_label_color(board):
    return board_color_map[board]
