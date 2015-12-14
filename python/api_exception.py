from sqlalchemy.exc import SQLAlchemyError
from appfile import app
from flask import jsonify

# error code
ERROR_SQLALCHEMY =1801

@app.errorhandler(SQLAlchemyError)
def handle_invalid_usage(error):
    response = jsonify(results = str(error))
    response.status_code = ERROR_SQLALCHEMY
    return response
