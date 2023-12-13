<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Color</title>
</head>
<body>
    <h1>Add Color</h1>
    <form action="/colors/add" method="post">
        <label for="color_name">Name:</label>
        <input type="text" id="color_name" name="color_name" required>
        <br>
        <label for="flower_id">Flower:</label>
        <select id="flower_id" name="flower_id" required>
            % for flower in flowers:
                <option value="{{ flower[0] }}">{{ flower[1] }}</option>
            % end
        </select>
        <br>
        <input type="submit" value="Add Color">
    </form>
    <p><a href="/colors">Back to Colors</a></p>
</body>
</html>
