@extends('device.index')
@section('tab')

<html>
<head>
	<title> Clickable Button </title>
</head>
<body>

<form method = "post" action="">
	@csrf
	<button type = "submit" name = "myButton" style = "border: 2px solid #000; padding: 5px;"> Click for Oneclick Diagnostics</button>
</form>

  <?php
	if (isset($_POST['myButton'])) {
		sleep(2);
    echo "RP/0/RP0/CPU0:dream#show version";
    echo "Cisco IOS XR Software, Version 7.0.2 LNT"
    echo "Copyright (c) 2013-2020 by Cisco Systems, Inc.";
    echo "Build Inforamtion:";
    echo " Built By   : ahoang";
    echo " Built On   : Sat Mar 14 04:54:04 UTC 2020";
    echo " Built Host : iox-usc-029";
    echo " Workspace  : /auto/srcarchive15/prod/7.0.2/nsc540l/ws";
    echo " Version    :7.0.2";
    echo " Label      :7.0.2";
    echo "cisco NCS540L (C37708 @ 1.70GHz)";
    echo "System uptime is 0 weeks, 0 days, 0 hours, 5 minutes";
    echo "RP/0/RP0/CPU0:dream#show 12vpn xconnect";
    echo "RP/0/RP0/CPU0:dream#show 12vpn bridge-domain";
    echo "RP/0/RP0/CPU0:dream#show bdf session";
    echo "% No such configuration item(s)";
    
	}
?>

</body>
</html>

@endsection
