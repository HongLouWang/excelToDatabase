
namespace excelToDatabase {
    partial class Form1 {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.excelDataGridView = new System.Windows.Forms.DataGridView();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.excelToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.databaseToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.dictionaryToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.loadExcelToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.databaseGridView2 = new System.Windows.Forms.DataGridView();
            this.recentExcelToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.newDatabaseConnectionToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.savedDatabaseToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.newDictionaryToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.savedDictionaryToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            ((System.ComponentModel.ISupportInitialize)(this.excelDataGridView)).BeginInit();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.databaseGridView2)).BeginInit();
            this.SuspendLayout();
            // 
            // excelDataGridView
            // 
            this.excelDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.excelDataGridView.Location = new System.Drawing.Point(0, 24);
            this.excelDataGridView.Name = "excelDataGridView";
            this.excelDataGridView.Size = new System.Drawing.Size(388, 405);
            this.excelDataGridView.TabIndex = 0;
            // 
            // menuStrip1
            // 
            this.menuStrip1.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.excelToolStripMenuItem,
            this.databaseToolStripMenuItem,
            this.dictionaryToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(800, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // excelToolStripMenuItem
            // 
            this.excelToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.loadExcelToolStripMenuItem,
            this.recentExcelToolStripMenuItem});
            this.excelToolStripMenuItem.Name = "excelToolStripMenuItem";
            this.excelToolStripMenuItem.Size = new System.Drawing.Size(46, 20);
            this.excelToolStripMenuItem.Text = "Excel";
            // 
            // databaseToolStripMenuItem
            // 
            this.databaseToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.newDatabaseConnectionToolStripMenuItem,
            this.savedDatabaseToolStripMenuItem});
            this.databaseToolStripMenuItem.Name = "databaseToolStripMenuItem";
            this.databaseToolStripMenuItem.Size = new System.Drawing.Size(67, 20);
            this.databaseToolStripMenuItem.Text = "Database";
            // 
            // dictionaryToolStripMenuItem
            // 
            this.dictionaryToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.newDictionaryToolStripMenuItem,
            this.savedDictionaryToolStripMenuItem});
            this.dictionaryToolStripMenuItem.Name = "dictionaryToolStripMenuItem";
            this.dictionaryToolStripMenuItem.Size = new System.Drawing.Size(73, 20);
            this.dictionaryToolStripMenuItem.Text = "Dictionary";
            // 
            // loadExcelToolStripMenuItem
            // 
            this.loadExcelToolStripMenuItem.Name = "loadExcelToolStripMenuItem";
            this.loadExcelToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.loadExcelToolStripMenuItem.Text = "Load Excel";
            // 
            // databaseGridView2
            // 
            this.databaseGridView2.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.databaseGridView2.Location = new System.Drawing.Point(412, 24);
            this.databaseGridView2.Name = "databaseGridView2";
            this.databaseGridView2.Size = new System.Drawing.Size(388, 405);
            this.databaseGridView2.TabIndex = 2;
            // 
            // recentExcelToolStripMenuItem
            // 
            this.recentExcelToolStripMenuItem.Name = "recentExcelToolStripMenuItem";
            this.recentExcelToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.recentExcelToolStripMenuItem.Text = "Recent Excel";
            // 
            // newDatabaseConnectionToolStripMenuItem
            // 
            this.newDatabaseConnectionToolStripMenuItem.Name = "newDatabaseConnectionToolStripMenuItem";
            this.newDatabaseConnectionToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
            this.newDatabaseConnectionToolStripMenuItem.Text = "New Database Connection";
            // 
            // savedDatabaseToolStripMenuItem
            // 
            this.savedDatabaseToolStripMenuItem.Name = "savedDatabaseToolStripMenuItem";
            this.savedDatabaseToolStripMenuItem.Size = new System.Drawing.Size(221, 22);
            this.savedDatabaseToolStripMenuItem.Text = "Saved Database Connection";
            // 
            // newDictionaryToolStripMenuItem
            // 
            this.newDictionaryToolStripMenuItem.Name = "newDictionaryToolStripMenuItem";
            this.newDictionaryToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.newDictionaryToolStripMenuItem.Text = "New Dictionary";
            // 
            // savedDictionaryToolStripMenuItem
            // 
            this.savedDictionaryToolStripMenuItem.Name = "savedDictionaryToolStripMenuItem";
            this.savedDictionaryToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.savedDictionaryToolStripMenuItem.Text = "Saved Dictionary";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 429);
            this.Controls.Add(this.databaseGridView2);
            this.Controls.Add(this.excelDataGridView);
            this.Controls.Add(this.menuStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MainMenuStrip = this.menuStrip1;
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.Text = "Excel To Database";
            ((System.ComponentModel.ISupportInitialize)(this.excelDataGridView)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.databaseGridView2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView excelDataGridView;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem excelToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem databaseToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem dictionaryToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem loadExcelToolStripMenuItem;
        private System.Windows.Forms.DataGridView databaseGridView2;
        private System.Windows.Forms.ToolStripMenuItem recentExcelToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem newDatabaseConnectionToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem savedDatabaseToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem newDictionaryToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem savedDictionaryToolStripMenuItem;
    }
}

