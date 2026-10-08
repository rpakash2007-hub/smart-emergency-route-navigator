from backend.app import app

if __name__ == "__main__":
    # Disable the Werkzeug reloader on Windows to avoid WinError 10038
    app.run(debug=True, use_reloader=False)
