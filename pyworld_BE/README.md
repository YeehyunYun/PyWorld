# sqlalchemy
객체 관계 매핑(Object Relational Mapping).
DB 테이블을 파이썬의 클래스로 표현해주고 파이썬 문법으로 sql 문을 작성할 수 있음

# pydantic
Python type hints를 사용하여 데이터의 유효성을 검사하는 라이브러리

### ORM mode
pydantic의 BaseModel -> OrmModel
https://docs.pydantic.dev/latest/concepts/models/
```python 
model_config = ConfigDict(from_attributes=True)
```
### Validator
Pydantic은 Annotated를 사용하여 유효성을 검사한다
https://docs.pydantic.dev/latest/concepts/validators/
```python 
def ts_si_down(ts: int):
    return ts * 1000

SecToMilliSecTs = Annotated[int, Ge(0), AfterValidator(ts_si_down)]
```