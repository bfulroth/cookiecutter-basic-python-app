from {{cookiecutter.script_slug}}.cli import run_main


if __name__ == '__main__':

    # Load environmental variables
    from dotenv import load_dotenv
    load_dotenv()
    run_main()