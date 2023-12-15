# Fix the WordPress file wp-settings.php to replace 'phpp' with 'php'

exec { 'fix_wp_settings_path':
  command => 'sed -i "137s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin']
}
