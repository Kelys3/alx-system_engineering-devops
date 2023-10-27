# A manifest that Kills the process named Killmenow

exec { 'kill_killmenow_process':
command  => 'pkill killmenow',
provider => 'shell',
}
