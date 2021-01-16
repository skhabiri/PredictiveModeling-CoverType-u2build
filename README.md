# forestcover_metrics

This is a Classifiers metrics for forest cover_type dataset. It's
a plotly dash app deployed on Heroku. Estimators data have been saved as pkl file.


### Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

```bash
pip install -r requirements/dev.txt
```

Once you have installed the project dependencies you can run the app locally with the command

``flask run``

## Deployment to Heroku

You should familiarize yourself with the basic [Git](https://git-scm.com/) and [Heroku](https://heroku.com/) concepts before
  deploying this app. 

Application configuration is in `app.json` and you should be able to deploy using

<a href="https://heroku.com/deploy" style="display: block"><img src="https://www.herokucdn.com/deploy/button.svg" title="Deploy" alt="Deploy"></a>
    <br>

Deployment by using [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):

If you're unable to successfully deploy using the button you will need to try using the CLI.


### What does the app do:
Accuracy, Precision, and Recall scores of all five fitted estimators are pickled. Plotly dash framework is used to design the layout, and features of the web base app. In the app we can select several estimators and metrics. The loaded pickle file is used to output a report of the selected metrics for side by side comparison.

### Create a new Heroku App.
Create an app in heroku.com
#heroku create predictivemodeling-covertype
Install heroku command line on local machine

```
$ heroku login #establish SSH key to heroku account
$ cd my-project/
$ git init 		#If the directory has not already initialized as a git directory
$ heroku git:remote -a predictivemodeling-covertype	#add a remote handle to heroku
$ git add .
$ git commit -am "make it better"
```

### Deploy on Heroku by pushing to the heroku branch
```
$ git push heroku master	#deploy it to Heroku using Git.
```

To speed up the testing process, we run the app locally by `$flask run`, before deploying it to heroku. 

### App structure: 
**run.py:**
- server = create_app(); server.run_server()

**app:**
- Init.py:
    - def create_app():
app = flask.Flask(__name__); register_dashboard(app); return app
- dashboard.py:
    - def register_dashboard(server): returns dashboard
dashboard = dash.Dash(): url_base_pathname, server
dashboard.layout = html.Div() : navbar, page-content, footer
server.app_context(): register_callbacks(dashboard)
- callback.py:
    - register_callbacks(app):
@app.callback(Output("page-content"), Input("pathname"))
def display_page(pathname)
@app.callback(Output("report_output"), Input("Compute", "n_clicks"), State('est_dropdown1'), State('score_checkbox1'))
def update_output(n_clicks, dropval, boxval): return my_string
- components:
    - footer.py, navbar.py
- page:
    - index.py (root route)
        - dbc.Button("Prediction Metrics"), dbc.Row(html.Img())
    - predictions.py
        - dbc.Card("Summary")), dcc.Dropdown("est_dropdown1"), dcc.Checklist("score_checkbox1"), dbc.Button("Compute"), dcc.Textarea("report_output")
    - process.py, insights.py

