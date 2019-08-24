classdef byeongkwanPower_exported < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure                       matlab.ui.Figure
        UIAxes                         matlab.ui.control.UIAxes
        RealtimeOccupantsStateVisualizingSystemLabel  matlab.ui.control.Label
        ServicedbyTeamPalisadeLabel    matlab.ui.control.Label
        Button                         matlab.ui.control.Button
        UIAxes2                        matlab.ui.control.UIAxes
        MouthPanel                     matlab.ui.container.Panel
        heightLabel_3                  matlab.ui.control.Label
        lip_height                     matlab.ui.control.TextArea
        widthLabel                     matlab.ui.control.Label
        lip_width                      matlab.ui.control.TextArea
        upperLabel                     matlab.ui.control.Label
        lip_upper                      matlab.ui.control.TextArea
        underLabel                     matlab.ui.control.Label
        lip_under                      matlab.ui.control.TextArea
        EyePanel                       matlab.ui.container.Panel
        widthTextArea_4Label           matlab.ui.control.Label
        eye_width                      matlab.ui.control.TextArea
        heightLabel                    matlab.ui.control.Label
        eye_height                     matlab.ui.control.TextArea
        EmotionPanel                   matlab.ui.container.Panel
        neutralTextAreaLabel           matlab.ui.control.Label
        neutralTextArea                matlab.ui.control.TextArea
        angerTextAreaLabel             matlab.ui.control.Label
        angerTextArea                  matlab.ui.control.TextArea
        happinessTextAreaLabel         matlab.ui.control.Label
        happinessTextArea              matlab.ui.control.TextArea
        disgustTextAreaLabel           matlab.ui.control.Label
        disgustTextArea                matlab.ui.control.TextArea
        surpriseTextAreaLabel          matlab.ui.control.Label
        surpriseTextArea               matlab.ui.control.TextArea
        UIAxes3                        matlab.ui.control.UIAxes
        InfoPanel                      matlab.ui.container.Panel
        TextArea                       matlab.ui.control.TextArea
        OnlyforMatlab2019aLabel        matlab.ui.control.Label
        Serverurlhttp18236662325365Label  matlab.ui.control.Label
        AWSEC2c5lagrgeubuntu1604Label  matlab.ui.control.Label
        AWSRegionUSwest2bOregonLabel   matlab.ui.control.Label
        condition                      matlab.ui.control.TextArea
        AzureVirturalMachinesMScognitiveServiesLabel  matlab.ui.control.Label
        RegionAsiaCentralseoulLabel    matlab.ui.control.Label
        QAzaza8033gmailcomLabel        matlab.ui.control.Label
        Image                          matlab.ui.control.Image
        Image2                         matlab.ui.control.Image
        Image3                         matlab.ui.control.Image
    end

    
    properties (Access = public)
        pre_latest = "";
        img_url = "https://palisade5365.s3.ap-northeast-2.amazonaws.com/";
        url = 'http://18.236.66.232:5365/matrequest';
        plot_x = [];
        plot_neutral = [];
        plot_happiness = [];
        plot_anger = [];
        plot_disgust = [];
        plot_eye_width = [];
        plot_eye_height = [];
        plot_surprise = [];
        
        count = 0;
    end
    

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            disp('Hi!')
            
            app.UIAxes2.XLim = [0 30];
            app.UIAxes3.XLim = [0 30];
            app.TextArea.Value = 'Stopped';
            app.UIAxes2.YLim = [0 1];
            app.UIAxes3.YLim = [0 60];
            
            
        end

        % Button pushed function: Button
        function ButtonPushed2(app, event)
            app.TextArea.Value = 'Playing';
            flag = true;
            
            while (1)
                try
                    data = webread(app.url);
                catch
                    disp('Connection Failed');
                    app.condition.Value = 'Connection Failed';
                    flag = false;
                end
                if flag
                    if(data.code == '-1' | data.code == -1)
                        
                        if isfield(data,'latest')
                            disp(['latest file name = ', data.latest])
                            url_show = strcat(app.img_url, data.latest);
                            [url_img, map] = imread(url_show);
                            imshow(url_img,'parent',app.UIAxes);
                            app.neutralTextArea.Value = 'Null';
                            app.angerTextArea.Value = 'Null';
                            app.happinessTextArea.Value = 'Null';
                            app.disgustTextArea.Value = 'Null';
                            app.surpriseTextArea.Value = 'Null';
                            app.condition.Value = 'Cannot Found Face!';
                            pause(0.2)
                        end
                    elseif(app.pre_latest == data.latest)
                        disp(['latest file name = ', data.latest])
                        disp('Nothing to Update!')
                    else
                        
                        
                        
                        url_show = strcat(app.img_url, data.latest);
                        
                        [url_img, map] = imread(url_show);
                        [eye,brow,mouth,nose,pupil] = getPs(data);
                        color_nose = {'yellow';'yellow';'yellow';'yellow';'yellow';'yellow';'yellow'};
                        color_mouth = {'cyan';'cyan';'cyan';'cyan';'cyan';'cyan'};
                        
                        app.neutralTextArea.Value = num2str(data.emotion.neutral);
                        app.angerTextArea.Value = num2str(data.emotion.anger);
                        app.happinessTextArea.Value = num2str(data.emotion.happiness);
                        app.disgustTextArea.Value = num2str(data.emotion.disgust);
                        app.surpriseTextArea.Value = num2str(data.emotion.sadness);
                        
                        app.lip_upper.Value = num2str(mouth(5,2)-mouth(6,2));
                        app.lip_height.Value = num2str(mouth(4,2)-mouth(5,2));
                        app.lip_width.Value = num2str(mouth(2,1)-mouth(1,1));
                        app.lip_under.Value = num2str(mouth(3,2)-mouth(4,2));
                        
                        app.eye_height.Value = num2str((eye(1,2)-eye(4,2)+eye(5,2)-eye(8,2))/2);
                        app.eye_width.Value = num2str((eye(2,1)-eye(3,1)+eye(7,1)-eye(6,1))/2);
                        
                        
                        top = data.rectangle.top;
                        left = data.rectangle.left;
                        width = data.rectangle.width;
                        height = data.rectangle.height;
                        
                        imshow(url_img,'parent',app.UIAxes);
                        
                        eye_marked = insertMarker(url_img,eye,'o');
                        
                        
                        mouth_marked = insertMarker(eye_marked,mouth,'o','color',color_mouth);
                        
                        
                        
                        nose_marked = insertMarker(mouth_marked,nose,'o','color',color_nose);
                        imshow(nose_marked,'parent',app.UIAxes);
                        
                        app.condition.Value = '';
                        
                        
                        pause(0.1)
                        poly = insertShape(nose_marked, 'FilledPolygon',[nose(5,1) nose(5,2) nose(2,1) nose(2,2) nose(1,1) nose(1,2) nose(7,1) nose(7,2) nose(3,1) nose(3,2) nose(4,1) nose(4,2) nose(6,1) nose(6,2)],'Color','yellow');
                        imshow(poly,'parent',app.UIAxes);
                        
                        
                        pause(0.1)
                        lined = insertShape(poly, 'Line', [eye(2,1) eye(2,2) eye(3,1) eye(3,2);eye(6,1) eye(6,2) eye(7,1) eye(7,2);eye(1,1) eye(1,2) eye(4,1) eye(4,2);eye(5,1) eye(5,2) eye(8,1) eye(8,2)], 'Color','green','LineWidth',2);
                        imshow(lined,'parent',app.UIAxes);
                        
                        rect = insertShape(lined,"Line",[left top left (height+top) (left+width) (height+top) (left+width) top left top],'LineWidth',4,'Color',{"magenta"});
                        imshow(rect,'parent',app.UIAxes);
                        
                        app.pre_latest = data.latest;
                        %%%%%%%%%%%%%%%%%plot area%%%%%%%%%%%%%%%%%%%
                        app.plot_x = [app.plot_x, app.count];
                        app.count = app.count+1;
                        
                        app.plot_neutral = [app.plot_neutral, data.emotion.neutral];
                        app.plot_happiness = [app.plot_happiness, data.emotion.happiness];
                        app.plot_anger = [app.plot_anger; data.emotion.anger];
                        app.plot_disgust = [app.plot_disgust; data.emotion.disgust];
                        app.plot_surprise = [app.plot_surprise; data.emotion.surprise];
                        app.plot_eye_width = [app.plot_eye_width; (eye(2,1)-eye(3,1)+eye(7,1)-eye(6,1))/2];
                        app.plot_eye_height = [app.plot_eye_height; (eye(1,2)-eye(4,2)+eye(5,2)-eye(8,2))/2];
                        if app.count > 30
                            app.UIAxes2.XLim = [app.count-30 app.count];
                            app.UIAxes3.XLim = [app.count-30 app.count];
                        end
                    end
                        plot(app.UIAxes2, app.plot_x, app.plot_neutral,app.plot_x, app.plot_disgust, app.plot_x, app.plot_happiness, app.plot_x, app.plot_anger, app.plot_x, app.plot_surprise)
                        plot(app.UIAxes3, app.plot_x,app.plot_eye_width,app.plot_x,app.plot_eye_height)
                    if ischar(data.code)
                        cmd = int8(data.code);
                    else
                        cmd = data.code;
                    end
                    
                    if cmd == 2
                        app.condition.FontColor = 'black';
                        app.condition.Value = 'AI Prediction: Normal';
                        
                    elseif cmd == 3
                        app.condition.Value = 'AI Prediction: Sick';
                        app.condition.FontColor = 'r';
                        
                    elseif cmd == 4
                        app.condition.FontColor = 'black';
                        app.condition.Value = 'AI Prediction: Sleep';
                    else
                        disp('he');
                    end
                    
                    pause(0.2)
                    
                end
            end
            
            
        
        
        
        
        
 
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.AutoResizeChildren = 'off';
            app.UIFigure.Position = [0 1080 1920 1050];
            app.UIFigure.Name = 'UI Figure';

            % Create UIAxes
            app.UIAxes = uiaxes(app.UIFigure);
            title(app.UIAxes, '')
            xlabel(app.UIAxes, '')
            ylabel(app.UIAxes, '')
            app.UIAxes.PlotBoxAspectRatio = [1.07530120481928 1 1];
            app.UIAxes.GridAlpha = 0.15;
            app.UIAxes.MinorGridAlpha = 0.25;
            app.UIAxes.Box = 'on';
            app.UIAxes.XTick = [];
            app.UIAxes.YTick = [];
            app.UIAxes.Position = [1231 441 640 480];

            % Create RealtimeOccupantsStateVisualizingSystemLabel
            app.RealtimeOccupantsStateVisualizingSystemLabel = uilabel(app.UIFigure);
            app.RealtimeOccupantsStateVisualizingSystemLabel.HorizontalAlignment = 'center';
            app.RealtimeOccupantsStateVisualizingSystemLabel.FontSize = 35;
            app.RealtimeOccupantsStateVisualizingSystemLabel.FontWeight = 'bold';
            app.RealtimeOccupantsStateVisualizingSystemLabel.Position = [566 973 789 43];
            app.RealtimeOccupantsStateVisualizingSystemLabel.Text = 'Realtime Occupant''s State Visualizing System';

            % Create ServicedbyTeamPalisadeLabel
            app.ServicedbyTeamPalisadeLabel = uilabel(app.UIFigure);
            app.ServicedbyTeamPalisadeLabel.FontSize = 20;
            app.ServicedbyTeamPalisadeLabel.FontWeight = 'bold';
            app.ServicedbyTeamPalisadeLabel.Position = [1639 17 264 24];
            app.ServicedbyTeamPalisadeLabel.Text = 'Serviced by Team Palisade';

            % Create Button
            app.Button = uibutton(app.UIFigure, 'push');
            app.Button.ButtonPushedFcn = createCallbackFcn(app, @ButtonPushed2, true);
            app.Button.FontSize = 20;
            app.Button.Position = [1751 959 97 42];
            app.Button.Text = 'ÿÿ';

            % Create UIAxes2
            app.UIAxes2 = uiaxes(app.UIFigure);
            title(app.UIAxes2, 'Emotion')
            xlabel(app.UIAxes2, '')
            ylabel(app.UIAxes2, 'probability')
            app.UIAxes2.FontSize = 20;
            app.UIAxes2.XLim = [0 1];
            app.UIAxes2.XTick = [0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300];
            app.UIAxes2.XTickLabel = '';
            app.UIAxes2.LineWidth = 1.2;
            app.UIAxes2.Position = [11 301 1200 280];

            % Create MouthPanel
            app.MouthPanel = uipanel(app.UIFigure);
            app.MouthPanel.AutoResizeChildren = 'off';
            app.MouthPanel.TitlePosition = 'centertop';
            app.MouthPanel.Title = 'Mouth';
            app.MouthPanel.FontWeight = 'bold';
            app.MouthPanel.FontSize = 20;
            app.MouthPanel.Position = [691 721 520 200];

            % Create heightLabel_3
            app.heightLabel_3 = uilabel(app.MouthPanel);
            app.heightLabel_3.HorizontalAlignment = 'right';
            app.heightLabel_3.FontSize = 18;
            app.heightLabel_3.Position = [274 112 55 22];
            app.heightLabel_3.Text = 'height';

            % Create lip_height
            app.lip_height = uitextarea(app.MouthPanel);
            app.lip_height.HorizontalAlignment = 'center';
            app.lip_height.FontSize = 18;
            app.lip_height.Position = [354 106 125 34];

            % Create widthLabel
            app.widthLabel = uilabel(app.MouthPanel);
            app.widthLabel.HorizontalAlignment = 'right';
            app.widthLabel.FontSize = 18;
            app.widthLabel.Position = [281 43 48 22];
            app.widthLabel.Text = 'width';

            % Create lip_width
            app.lip_width = uitextarea(app.MouthPanel);
            app.lip_width.HorizontalAlignment = 'center';
            app.lip_width.FontSize = 18;
            app.lip_width.Position = [354 37 125 34];

            % Create upperLabel
            app.upperLabel = uilabel(app.MouthPanel);
            app.upperLabel.HorizontalAlignment = 'center';
            app.upperLabel.FontSize = 18;
            app.upperLabel.Position = [41 112 52 22];
            app.upperLabel.Text = 'upper';

            % Create lip_upper
            app.lip_upper = uitextarea(app.MouthPanel);
            app.lip_upper.HorizontalAlignment = 'center';
            app.lip_upper.FontSize = 18;
            app.lip_upper.Position = [118 106 125 34];

            % Create underLabel
            app.underLabel = uilabel(app.MouthPanel);
            app.underLabel.HorizontalAlignment = 'right';
            app.underLabel.FontSize = 18;
            app.underLabel.Position = [41 43 52 22];
            app.underLabel.Text = 'under';

            % Create lip_under
            app.lip_under = uitextarea(app.MouthPanel);
            app.lip_under.HorizontalAlignment = 'center';
            app.lip_under.FontSize = 18;
            app.lip_under.Position = [118 37 125 34];

            % Create EyePanel
            app.EyePanel = uipanel(app.UIFigure);
            app.EyePanel.AutoResizeChildren = 'off';
            app.EyePanel.TitlePosition = 'centertop';
            app.EyePanel.Title = 'Eye';
            app.EyePanel.FontWeight = 'bold';
            app.EyePanel.FontSize = 20;
            app.EyePanel.Position = [411 721 260 200];

            % Create widthTextArea_4Label
            app.widthTextArea_4Label = uilabel(app.EyePanel);
            app.widthTextArea_4Label.HorizontalAlignment = 'right';
            app.widthTextArea_4Label.FontSize = 18;
            app.widthTextArea_4Label.Position = [31 111 48 22];
            app.widthTextArea_4Label.Text = 'width';

            % Create eye_width
            app.eye_width = uitextarea(app.EyePanel);
            app.eye_width.HorizontalAlignment = 'center';
            app.eye_width.FontSize = 18;
            app.eye_width.Position = [104 103 125 34];

            % Create heightLabel
            app.heightLabel = uilabel(app.EyePanel);
            app.heightLabel.HorizontalAlignment = 'right';
            app.heightLabel.FontSize = 18;
            app.heightLabel.Position = [21 44 55 22];
            app.heightLabel.Text = 'height';

            % Create eye_height
            app.eye_height = uitextarea(app.EyePanel);
            app.eye_height.HorizontalAlignment = 'center';
            app.eye_height.FontSize = 18;
            app.eye_height.Position = [101 37 125 34];

            % Create EmotionPanel
            app.EmotionPanel = uipanel(app.UIFigure);
            app.EmotionPanel.AutoResizeChildren = 'off';
            app.EmotionPanel.TitlePosition = 'centertop';
            app.EmotionPanel.Title = 'Emotion';
            app.EmotionPanel.FontWeight = 'bold';
            app.EmotionPanel.FontSize = 20;
            app.EmotionPanel.Position = [41 591 1170 120];

            % Create neutralTextAreaLabel
            app.neutralTextAreaLabel = uilabel(app.EmotionPanel);
            app.neutralTextAreaLabel.HorizontalAlignment = 'right';
            app.neutralTextAreaLabel.FontSize = 20;
            app.neutralTextAreaLabel.Position = [20 34 67 24];
            app.neutralTextAreaLabel.Text = 'neutral';

            % Create neutralTextArea
            app.neutralTextArea = uitextarea(app.EmotionPanel);
            app.neutralTextArea.HorizontalAlignment = 'center';
            app.neutralTextArea.FontSize = 20;
            app.neutralTextArea.Position = [102 31 125 30];

            % Create angerTextAreaLabel
            app.angerTextAreaLabel = uilabel(app.EmotionPanel);
            app.angerTextAreaLabel.HorizontalAlignment = 'right';
            app.angerTextAreaLabel.FontSize = 20;
            app.angerTextAreaLabel.Position = [461 34 57 24];
            app.angerTextAreaLabel.Text = 'anger';

            % Create angerTextArea
            app.angerTextArea = uitextarea(app.EmotionPanel);
            app.angerTextArea.HorizontalAlignment = 'center';
            app.angerTextArea.FontSize = 20;
            app.angerTextArea.Position = [534 31 125 30];

            % Create happinessTextAreaLabel
            app.happinessTextAreaLabel = uilabel(app.EmotionPanel);
            app.happinessTextAreaLabel.HorizontalAlignment = 'right';
            app.happinessTextAreaLabel.FontSize = 20;
            app.happinessTextAreaLabel.Position = [911 34 97 24];
            app.happinessTextAreaLabel.Text = 'happiness';

            % Create happinessTextArea
            app.happinessTextArea = uitextarea(app.EmotionPanel);
            app.happinessTextArea.HorizontalAlignment = 'center';
            app.happinessTextArea.FontSize = 20;
            app.happinessTextArea.Position = [1023 31 125 30];

            % Create disgustTextAreaLabel
            app.disgustTextAreaLabel = uilabel(app.EmotionPanel);
            app.disgustTextAreaLabel.HorizontalAlignment = 'right';
            app.disgustTextAreaLabel.FontSize = 20;
            app.disgustTextAreaLabel.Position = [241 34 69 24];
            app.disgustTextAreaLabel.Text = 'disgust';

            % Create disgustTextArea
            app.disgustTextArea = uitextarea(app.EmotionPanel);
            app.disgustTextArea.HorizontalAlignment = 'center';
            app.disgustTextArea.FontSize = 20;
            app.disgustTextArea.Position = [327 31 125 30];

            % Create surpriseTextAreaLabel
            app.surpriseTextAreaLabel = uilabel(app.EmotionPanel);
            app.surpriseTextAreaLabel.HorizontalAlignment = 'right';
            app.surpriseTextAreaLabel.FontSize = 20;
            app.surpriseTextAreaLabel.Position = [674 34 77 24];
            app.surpriseTextAreaLabel.Text = 'surprise';

            % Create surpriseTextArea
            app.surpriseTextArea = uitextarea(app.EmotionPanel);
            app.surpriseTextArea.HorizontalAlignment = 'center';
            app.surpriseTextArea.FontSize = 20;
            app.surpriseTextArea.Position = [771 31 125 30];

            % Create UIAxes3
            app.UIAxes3 = uiaxes(app.UIFigure);
            title(app.UIAxes3, '')
            xlabel(app.UIAxes3, '')
            ylabel(app.UIAxes3, 'pixel')
            app.UIAxes3.FontSize = 20;
            app.UIAxes3.XLim = [0 1];
            app.UIAxes3.XTickLabel = '';
            app.UIAxes3.YTick = [0 30 60];
            app.UIAxes3.YTickLabel = {'0'; '30'; '60'};
            app.UIAxes3.LineWidth = 1.2;
            app.UIAxes3.Position = [11 19 1200 280];

            % Create InfoPanel
            app.InfoPanel = uipanel(app.UIFigure);
            app.InfoPanel.AutoResizeChildren = 'off';
            app.InfoPanel.TitlePosition = 'centertop';
            app.InfoPanel.Title = 'Info';
            app.InfoPanel.FontWeight = 'bold';
            app.InfoPanel.FontSize = 20;
            app.InfoPanel.Position = [42 721 349 200];

            % Create TextArea
            app.TextArea = uitextarea(app.InfoPanel);
            app.TextArea.HorizontalAlignment = 'center';
            app.TextArea.FontSize = 20;
            app.TextArea.Position = [101 131 150 30];

            % Create OnlyforMatlab2019aLabel
            app.OnlyforMatlab2019aLabel = uilabel(app.InfoPanel);
            app.OnlyforMatlab2019aLabel.Position = [11 91 126 30];
            app.OnlyforMatlab2019aLabel.Text = 'Only for Matlab 2019a';

            % Create Serverurlhttp18236662325365Label
            app.Serverurlhttp18236662325365Label = uilabel(app.InfoPanel);
            app.Serverurlhttp18236662325365Label.Position = [11 63 214 30];
            app.Serverurlhttp18236662325365Label.Text = 'Server url : http://18.236.66.232:5365';

            % Create AWSEC2c5lagrgeubuntu1604Label
            app.AWSEC2c5lagrgeubuntu1604Label = uilabel(app.InfoPanel);
            app.AWSEC2c5lagrgeubuntu1604Label.Position = [12 34 214 30];
            app.AWSEC2c5lagrgeubuntu1604Label.Text = 'AWS EC2 : c5.lagrge  , ubuntu 16.04';

            % Create AWSRegionUSwest2bOregonLabel
            app.AWSRegionUSwest2bOregonLabel = uilabel(app.InfoPanel);
            app.AWSRegionUSwest2bOregonLabel.Position = [11 5 214 30];
            app.AWSRegionUSwest2bOregonLabel.Text = 'AWS Region :US-west-2b (Oregon)';

            % Create condition
            app.condition = uitextarea(app.UIFigure);
            app.condition.HorizontalAlignment = 'center';
            app.condition.FontSize = 35;
            app.condition.Position = [1313 65 475 75];

            % Create AzureVirturalMachinesMScognitiveServiesLabel
            app.AzureVirturalMachinesMScognitiveServiesLabel = uilabel(app.UIFigure);
            app.AzureVirturalMachinesMScognitiveServiesLabel.Position = [1313 377 253 30];
            app.AzureVirturalMachinesMScognitiveServiesLabel.Text = 'Azure Virtural Machines, MS cognitive Servies';

            % Create RegionAsiaCentralseoulLabel
            app.RegionAsiaCentralseoulLabel = uilabel(app.UIFigure);
            app.RegionAsiaCentralseoulLabel.Position = [1313 348 214 30];
            app.RegionAsiaCentralseoulLabel.Text = 'Region : Asia Central (seoul)';

            % Create QAzaza8033gmailcomLabel
            app.QAzaza8033gmailcomLabel = uilabel(app.UIFigure);
            app.QAzaza8033gmailcomLabel.Position = [1313 319 214 30];
            app.QAzaza8033gmailcomLabel.Text = 'Q&A: zaza8033@gmail.com';

            % Create Image
            app.Image = uiimage(app.UIFigure);
            app.Image.Position = [1313 165 120 120];
            app.Image.ImageSource = 'KakaoTalk_20190822_101537473.png';

            % Create Image2
            app.Image2 = uiimage(app.UIFigure);
            app.Image2.Position = [1491 165 120 120];
            app.Image2.ImageSource = 'KakaoTalk_20190822_102043929.png';

            % Create Image3
            app.Image3 = uiimage(app.UIFigure);
            app.Image3.Position = [1668 165 120 120];
            app.Image3.ImageSource = 'T--TecCEM--Sponsors5.png';

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = byeongkwanPower_exported

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end
