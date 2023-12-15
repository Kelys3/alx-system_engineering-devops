# Fix the WordPress file wp-settings.php to replace 'phpp' with 'php'

exec { 'fix-wordpress':
  command => 'sed -i "137s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
