#   todo:
#   DB таблица user минимальная
#   filesharing
#
#   service -- внутрянка - локальное хранилище для файлов
#   read SQL DB | db таблицы ORM + migration
#
#   добавить @servak.exception_handler декоратор
#   написание unit тестов
#   async + Starlette
#   deploy CI/CD + DOCKER ( baza )


"""
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


"""