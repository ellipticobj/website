if tmux has-session -t website; then
	tmux kill-session -t website;
fi

tmux new -d -s website "cd ~/pub/ && git pull && python3 app.py";
