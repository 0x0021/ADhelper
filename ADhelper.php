<meta charset="utf-8">
<?php
session_start();
header("Content-type: text/html; charset=utf-8");

if ($_POST['type'] == 'unlockaccount') {
	$cmd = "python .\cgi-bin\ADunlock.py {$_POST['code']}";
	$result=exec($cmd,$results,$flag);
	#flag等0且返回值不为false时才是脚本执行成功
	if ($flag == 0 && $result != 'false') {
		#$_SESSION['user_id']=$results[0];
		#$_SESSION['dept_id']=$results[1];
		echo '账户解锁成功';
	}
	else {
		echo "账号解锁失败,请联系管理员<br>";
		echo $results[0];
	}
}
else if ($_POST['type'] == 'resetpassword') {
	$cmd = "python .\cgi-bin\ADResetPassword.py {$_POST['code']}";
	$result=exec($cmd,$results,$flag);
	#flag等0且返回值不为false时才是脚本执行成功
	if ($flag == 0 && $result != 'false') {
	#$_SESSION['user_id']=$results[0];
	#$_SESSION['dept_id']=$results[1];
	echo "密码已重置为mkgz18//";
	}
	else {
		echo "密码重置失败,请联系管理员<br>";
		echo $results[0];
	}
}
else {
	echo "操作类型异常,请联系管理员<br>";
}
?>