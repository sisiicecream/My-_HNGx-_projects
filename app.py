from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/get-specific-info')
def get_specific_info():
    # Get the query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get the current UTC time
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get the GitHub file URL and GitHub repo URL 
    github_file_url = "https://github.com/sisiicecream/My-_HNGx-_projects/blob/main/app.py"
    github_repo_url = "https://github.com/sisiicecream/My-_HNGx-_projects"

    # Prepare the response JSON
    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
