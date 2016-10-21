from app import app
from app.routes.oauth import get_oauth_url


@app.context_processor
def inject_oauth():
    return {
        'oauth_req_url': get_oauth_url()
    }
