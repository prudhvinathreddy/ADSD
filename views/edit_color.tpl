<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Color</title>
</head>
<body>
    <h1>Edit Color</h1>
    <form action="/colors/edit/{{ color[0] }}" method="post">
        <label for="color_name">Name:</label>
        <input type="text" id="color_name" name="color_name" value="{{ color[1] }}" required>
        <br>
        <label for="flower_id">Flower:</label>
        <select id="flower_id" name="flower_id" required>
            % for flower in flowers:
                <option value="{{ flower[0] }}" % if flower[0] == color[2]: selected % end>{{ flower[1] }}</option>
            % end
        </select>
        <br>
        <input type="submit" value="Save Changes">
    </form>
    <p><a href="/colors">Back to Colors</a></p>
</body>
</html>
