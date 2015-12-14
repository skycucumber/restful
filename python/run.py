
from flask.ext.session import Session

import sse
import appfile
app = appfile.app

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)
auth = appfile.auth


import api_user
import api_gateway
import api_exception
import api_message

if __name__ == '__main__':
    app.run(debug=True,port= 5002)





