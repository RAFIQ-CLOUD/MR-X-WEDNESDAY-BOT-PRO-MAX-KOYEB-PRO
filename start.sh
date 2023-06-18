if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://RAFIQ-CLOUD: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@github.com/RAFIQ-CLOUD/MR-X-WEDNESDAY-BOT-PRO-MAX-KOYEB.git /MR-X-WEDNESDAY-BOT-PRO-MAX-KOYEB
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MR-X-WEDNESDAY-BOT-PRO-MAX-KOYEB
fi
cd /MR-X-WEDNESDAY-BOT-PRO-MAX-KOYEB
pip3 install -U -r requirements.txt
echo "MR-X-WEDNESDAY-BOT-PRO-MAX STARTED...."
python3 bot.py
