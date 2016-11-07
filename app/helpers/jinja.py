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


project_status_content = {
    'waiting': {
        'style': 'ellipsis horizontal',
        'message': '분석 대기중'
    },
    'working': {
        'style': 'spinner',
        'message': '분석중입니다...'
    },
    'done': {
        'style': 'checkmark green',
        'message': '분석 완료!!'
    },
    'error': {
        'style': 'remove red',
        'message': '분석중 문제 발생'
    }
}


@app.add_template_filter
def project_status_style(status):
    return project_status_content[status]['style']


@app.add_template_filter
def project_status_message(status):
    return project_status_content[status]['message']
