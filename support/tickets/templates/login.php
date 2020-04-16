<form method="POST">
    {% csrf_token %}
    <p>Логин <input name="login" type="text" style="color: #5d5d5d; width: 15%; padding: 4px;"><br></p>
    <p>Пароль <input name="password" type="password" style="color: #5d5d5d; width: 15%; padding: 4px;"><br></p>
    <p>Не прикреплять к IP(не безопасно) <input type="checkbox" name="not_attach_ip"><br></p>
    <p><input name="submit" type="submit" value="Войти" style=" padding: 8px; background-color: white;
    cursor: pointer; width: 100px;"></p>
</form>