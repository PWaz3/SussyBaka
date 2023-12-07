@extends('device.index')
@section('tab')

<html>
<head>
    <title>Clickable Button</title>
</head>
<body>

<form method="post" action="{{ route('executePythonScript') }}">
    @csrf
    <button type="submit" name="myButton" style = "border: 2px solid #000; padding: 5px;">Click for Oneclick Diagnostics</button>
</form>

</body>
</html>

@endsection
