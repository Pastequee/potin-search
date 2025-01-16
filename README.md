# Welcome to Potin Search

The goal here was to make a very quick "search engine" using semantic search on a dataset of articles

## How to run ?

### Using Docker

Just run the command

```bash
docker compose --build -up -d
```

And you can now view the website on the following URL

```bash
http://localhost:3000/
```

To stop the containers just do
```bash
docker compose down
```

### By hand

#### Step 1: Scrap the article using the script

Create a python venv using at the root of the `flask-api` directory
*BE CAREFULL, it will only work with Python 3.9+ until Python 3.12*
```bash
python -m venv .venv
```
Then use is
```bash
source .venv/bin/activate
```

After that you can install all the required libraries
```bash
pip install -r requirements.txt
```

And now you can run the script !
```bash
python3 scrapper/main.py
```

### Step 2: Start the Flask API

Just run the command
```bash
flask --app app run
```

### Step 3: Start the Next.js frontend

First of all, install all the node dependancies using your favourite package manager (I'm using pnpm)
```bash
pnpm install
```

Then you can just start the developpement server like so
```bash
pnpm run dev
```

Or build the project and running it in a more production ready manner
```bash
pnpm run build
pnpm run start
```

And you can now access the website at the following URL
```bash
http://localhost:3000
```
