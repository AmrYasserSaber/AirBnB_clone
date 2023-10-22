for i in $@;do
	touch $i
	code -r $i
done