#!/usr/bin/env ruby
# print ruby script
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
