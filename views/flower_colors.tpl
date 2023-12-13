<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flower Colors</title>
</head>
<body>
    <h1>Colors for Flower ID {{ flower_id }}</h1>
    <ul>
        % for color in colors:
            <li>{{ color[0] }}</li>
        % end
    </ul>
    <p><a href="/flowers">Back to Flowers</a></p>
</body>
</html>
