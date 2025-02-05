from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from fast_zero.models import Todo
from fast_zero.schemas import (
    Message,
    TodoFilter,
    TodoList,
    TodoPublic,
    TodoSchema,
    TodoUpdate,
)
from fast_zero.typing import T_CurrentUser, T_Session

todo_router = APIRouter(
    prefix='/todos',
    tags=['todos'],
)


@todo_router.post('/', response_model=TodoPublic)
def create_todo(todo: TodoSchema, session: T_Session, user: T_CurrentUser):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@todo_router.get('/', response_model=TodoList)
def list_todos(
    session: T_Session, user: T_CurrentUser, filters: TodoFilter = Depends()
):
    query = select(Todo).where(Todo.user_id == user.id)

    if filters.title:
        query = query.filter(Todo.title.contains(filters.title))

    if filters.description:
        query = query.filter(Todo.description.contains(filters.description))

    if filters.state:
        query = query.filter(Todo.state == filters.state)

    todos = session.scalars(
        query.offset(filters.offset).limit(filters.limit)
    ).all()
    return {'todos': todos}


@todo_router.delete('/{todo_id}', response_model=Message)
def delete_todo(todo_id: int, session: T_Session, user: T_CurrentUser):
    db_todo = session.scalar(
        select(Todo).where(Todo.id == todo_id, Todo.user_id == user.id)
    )

    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Todo not found',
        )
    session.delete(db_todo)
    session.commit()
    return {'message': 'Todo deleted'}


@todo_router.patch('/{todo_id}', response_model=TodoPublic)
def patch_todo(
    todo_id: int, todo: TodoUpdate, session: T_Session, user: T_CurrentUser
):
    db_todo = session.scalar(
        select(Todo).where(Todo.id == todo_id, Todo.user_id == user.id)
    )

    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Todo not found',
        )

    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo
