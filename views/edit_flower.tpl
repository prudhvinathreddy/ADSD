<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Flower</title>
</head>
<body>
    <h1>Edit Flower</h1>
    <form action="/flowers/edit/{{ flower[0] }}" method="post">
        <label for="flower_name">Name:</label>
        <input type="text" id="flower_name" name="flower_name" value="{{ flower[1] }}" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" rows="4" required>{{ flower[2] }}</textarea>
        <br>
        <input type="submit" value="Save Changes">
    </form>
    <p><a href="/flowers">Back to Flowers</a></p>
</body>
</html>
