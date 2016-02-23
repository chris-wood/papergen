require 'after_the_deadline'
require 'espeak'
require 'tts'

include ESpeak

AfterTheDeadline.set_api_key("12340fhasbdjhasbd")
File.open(ARGV[0], "r") do |f|
  f.each_line do |line|
    puts line
    result = AfterTheDeadline.check(line)
    puts result
    sleep(1)
    # speech = Speech.new(line)
    # speech.speak
    #line.play("en", 2)
  end
end
