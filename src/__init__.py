from flask import Flask,request,render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app():
    # สร้าง app (core server) ภายในไฟล์
    app = Flask(__name__)

    # Config app
    app.config["JSON_SORT_KEYS"] = False

    limiter = Limiter(
        app,
        key_func=get_remote_address,

        # set default limit 
        default_limits=["1000 per day", "1 per second"],
    )
    # Binds the application only
    with app.app_context():

        # import file bluprint ex. emp.py

        from .controllers import report
        app.register_blueprint(report.report_bp, url_prefix="/api/v2/report")

        
    # set route path 
    @app.route('/')
    def index():
        return render_template("index.htm")

    return app