import uvicorn



if __name__ == "__main__":
    uvicorn.run("app.app:app", port = 8000, reload = True)
    # set reload to False if you want to deploy your app