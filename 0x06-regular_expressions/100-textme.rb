#!/usr/bin/env ruby
# print ruby script
str = ARGV[0].scan(/\[([^\]([TFSu])]*)\]/).join(", ")
str.split(/\w+:(.*), to:(.*), flags:(.*)/)
puts str
