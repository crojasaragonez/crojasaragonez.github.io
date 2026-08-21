RESUME_DIR := resume
RESUME_TEX := carlos-rojas-resume.tex
RESUME_PDF := carlos-rojas-resume.pdf
PUBLIC_PDF := public/resume.pdf

.PHONY: all resume clean

all: resume

resume: $(PUBLIC_PDF)

$(PUBLIC_PDF): $(RESUME_DIR)/$(RESUME_TEX) $(RESUME_DIR)/altacv.cls $(RESUME_DIR)/carlos.jpg
	cd $(RESUME_DIR) && xelatex -interaction=nonstopmode -halt-on-error $(RESUME_TEX)
	cd $(RESUME_DIR) && xelatex -interaction=nonstopmode -halt-on-error $(RESUME_TEX)
	cp $(RESUME_DIR)/$(RESUME_PDF) $(PUBLIC_PDF)

clean:
	rm -f $(RESUME_DIR)/carlos-rojas-resume.aux $(RESUME_DIR)/carlos-rojas-resume.log $(RESUME_DIR)/carlos-rojas-resume.out $(RESUME_DIR)/$(RESUME_PDF) $(PUBLIC_PDF)
